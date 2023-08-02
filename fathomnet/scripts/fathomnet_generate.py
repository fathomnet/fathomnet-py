"""
fathomnet-generate: Generate a dataset from FathomNet localizations.
"""

import argparse
import os
import logging
import datetime
from typing import Iterable, List, Optional
from dataclasses import dataclass, replace
import requests
from shutil import copyfileobj
import progressbar

from coco_lib.common import Info as COCOInfo, Image as COCOImage, License as COCOLicense
from coco_lib.objectdetection import (
    ObjectDetectionAnnotation,
    ObjectDetectionCategory,
    ObjectDetectionDataset,
)

from ..api import images, taxa, darwincore
from ..dto import AImageDTO, GeoImageConstraints


@dataclass
class Arguments:
    """Parsed command-line arguments"""

    output: str
    concepts: List[str]
    base_constraints: GeoImageConstraints
    include_all: bool
    format: str
    img_dir: str


def comma_list(s: str) -> List[str]:
    """Parse a comma-separated list of strings"""
    return s.split(',')


def lowercase_str(s: str) -> str:
    """Convert a string to lowercase"""
    return s.lower()


def find_images_paged(
    constraints: GeoImageConstraints, page_size: int = 100
) -> Iterable[AImageDTO]:
    """Find images for a given constraints object, paginating requests at a given size"""
    offset = 0
    while True:
        constraints_page = replace(constraints, limit=page_size, offset=offset)
        images_page = images.find(constraints_page)

        for image in images_page:
            yield image

        if len(images_page) < page_size:
            break
        offset += page_size


def generate_constraints(
    concepts: List[str], base_constraints: GeoImageConstraints
) -> Iterable[GeoImageConstraints]:
    """Generate GeoImageConstraints instances for a list of concepts from a base set of constraints"""
    for concept in concepts:
        yield replace(base_constraints, concept=concept)


def write_voc(image: AImageDTO, filename: str):
    """Write a single image to a file"""
    with open(filename, 'w') as f:
        f.write(image.to_pascal_voc(pretty_print=True))


def download_imgs(args: Arguments, ims: List[AImageDTO]):
    """Download a images to an output dir"""
    flag = 0  # keep track of how many image downloaded
    for image in progressbar.progressbar(ims):
        file_name = os.path.join(
            args.img_dir, f"{image.uuid}.{image.url.split('.')[-1]}"
        )

        # only download if the image does not exist in the outdir
        if not os.path.exists(file_name):
            resp = requests.get(image.url, stream=True)
            resp.raw.decode_content = True
            with open(file_name, 'wb') as f:
                copyfileobj(resp.raw, f)
            flag += 1

    logging.info(f"Downloaded {flag} new images to {args.img_dir}")


def get_images(args: Arguments) -> Optional[List[AImageDTO]]:
    """Get images for the dataset as specified"""
    # Are we counting only?
    counting = args.output is None

    image_uuid_dict = {}
    if args.concepts:  # Concepts specified, generate constraints for each
        # Print concepts specified
        logging.info('Concept(s) specified:')
        for concept in args.concepts:
            logging.info('- {}'.format(concept))

        # Get the image data
        logging.info(
            'Fetching image records for {} concept(s)...'.format(len(args.concepts))
        )
        for constraints in generate_constraints(args.concepts, args.base_constraints):
            logging.debug('Constraints: {}'.format(constraints.to_json(indent=2)))
            concept_images = find_images_paged(constraints)
            for image in concept_images:
                image_uuid_dict[image.uuid] = image

        # Remove any unspecified bounding boxes from the images
        if not args.include_all:
            for image in image_uuid_dict.values():
                if image.boundingBoxes:
                    image.boundingBoxes = [
                        box
                        for box in image.boundingBoxes
                        if box.concept in args.concepts
                    ]
    else:  # No concepts specified, use the base constraints
        logging.info('Fetching image records...')
        noconcept_images = find_images_paged(args.base_constraints)
        for image in noconcept_images:
            image_uuid_dict[image.uuid] = image

    # Remove any images that don't have bounding boxes
    image_uuid_dict = {
        uuid: image for uuid, image in image_uuid_dict.items() if image.boundingBoxes
    }

    logging.info(
        'Found {} unique images with bounding boxes'.format(len(image_uuid_dict))
    )

    # Compute the number of bounding boxes per concept
    concept_counts = {}
    for image in image_uuid_dict.values():
        for box in image.boundingBoxes:
            concept_counts[box.concept] = concept_counts.get(box.concept, 0) + 1

    # Print table of bounding box counts for each concept
    if counting:
        if not concept_counts:
            print('No bounding boxes found')
        else:
            longest_concept = max(concept_counts.keys(), key=len)
            concept_header = 'concept'
            concept_len = len(longest_concept) + 1
            concept_len = max(concept_len, len(concept_header) + 1)

            count_header = '# boxes'
            count_len = 9
            count_len = max(count_len, len(count_header) + 1)

            format_str = '{:<' + str(concept_len) + '}|{:>' + str(count_len) + '}'

            print(format_str.format(concept_header, count_header))
            print(format_str.format('-' * concept_len, '-' * 9))
            for concept in sorted(concept_counts.keys()):
                count = concept_counts[concept]
                print(format_str.format(concept, count))

        return None
    else:
        return list(image_uuid_dict.values())


def generate_voc_dataset(ims: List[AImageDTO], output_dir: str) -> bool:
    """Generate a Pascal VOC dataset (folder of annotation XMLs)"""
    error_flag = False

    # Write images to output directory
    for image in ims:
        filename = '{}.{}'.format(image.uuid, 'xml')
        filename = os.path.join(output_dir, filename)
        logging.debug('Writing VOC {}'.format(filename))
        try:
            write_voc(image, filename)
        except OSError as e:
            logging.error('Error writing {}: {}'.format(filename, e))
            error_flag = True
    logging.info('Wrote {} VOC files to {}'.format(len(ims), output_dir))

    return error_flag


def generate_coco_dataset(ims: List[AImageDTO], output_dir: str) -> bool:
    # Describe the dataset
    coco_info = COCOInfo(
        year=datetime.datetime.now().year,
        version='0',
        description='Generated by FathomNet',
        contributor='FathomNet',
        url='https://fathomnet.org',
        date_created=datetime.datetime.now(),
    )

    # Set the FathomNet license
    fathomnet_license = COCOLicense(
        id=0, name='FathomNet', url='http://fathomnet.org/fathomnet/#/license'
    )

    # Encode categories in sorted order
    concepts = sorted(set(box.concept for image in ims for box in image.boundingBoxes))
    coco_categories = [
        ObjectDetectionCategory(id=idx, name=concept, supercategory='')
        for idx, concept in enumerate(concepts, start=1)
    ]

    # Encode images and annotations
    coco_images = []
    coco_annotations = []
    for image in ims:
        image_id = len(coco_images) + 1
        coco_image = COCOImage(
            id=image_id,
            width=image.width,
            height=image.height,
            file_name=f"{image.uuid}.{image.url.split('.')[-1]}",
            license=fathomnet_license.id,
            flickr_url=image.url,
            coco_url=image.url,
            date_captured=datetime.datetime.fromisoformat(image.timestamp.rstrip('Z'))
            if image.timestamp is not None
            else None,
        )
        coco_images.append(coco_image)

        for box in image.boundingBoxes:
            box_id = len(coco_annotations) + 1
            coco_annotation = ObjectDetectionAnnotation(
                id=box_id,
                image_id=image_id,
                category_id=concepts.index(box.concept) + 1,
                segmentation=[],
                area=float(box.width * box.height),
                bbox=[float(box.x), float(box.y), float(box.width), float(box.height)],
                iscrowd=0,
            )
            coco_annotations.append(coco_annotation)

    # Combine them into a dataset
    coco_dataset = ObjectDetectionDataset(
        info=coco_info,
        licenses=[fathomnet_license],
        images=coco_images,
        annotations=coco_annotations,
        categories=coco_categories,
    )

    # Write
    output_path = os.path.join(output_dir, 'dataset.json')
    try:
        coco_dataset.save(output_path, indent=2)
        logging.info('Wrote COCO dataset to {}'.format(output_path))
    except OSError as e:
        logging.error('Error writing {}: {}'.format(output_path, e))
        return True

    return False


def generate_dataset(args: Arguments, ims: List[AImageDTO]) -> bool:
    """Call the specified dataset generation function according to the format specified"""
    dataset_func = {'voc': generate_voc_dataset, 'coco': generate_coco_dataset}

    return dataset_func[args.format](ims, args.output)


def get_parser() -> argparse.ArgumentParser:
    """Set up the argument parser"""


def parse_args() -> Arguments:
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description=__doc__)

    valid_imaging_types = [t for t in images.list_imaging_types() if t is not None]
    valid_taxa_providers = taxa.list_taxa_providers()
    valid_contributor_emails = images.find_distinct_submitter()
    valid_owner_institution_codes = darwincore.find_owner_institution_codes()
    valid_dataset_formats = ['voc', 'coco']

    parser.add_argument('-v', action='count', default=0, help='Increase verbosity')
    parser.add_argument(
        '-t',
        '--taxa',
        dest='taxa',
        type=str,
        help='Taxonomy provider (to include descendants). Options: {}'.format(
            ', '.join(valid_taxa_providers)
        ),
    )
    parser.add_argument(
        '--contributor-email',
        dest='contributor_email',
        type=str,
        help='Contributor email',
    )
    parser.add_argument(
        '--start',
        dest='start_timestamp',
        type=datetime.datetime.fromisoformat,
        help='Start timestamp (formatted as ISO-8601)',
    )
    parser.add_argument(
        '--end',
        dest='end_timestamp',
        type=datetime.datetime.fromisoformat,
        help='End timestamp (formatted as ISO-8601)',
    )
    parser.add_argument(
        '--imaging-types',
        dest='imaging_types',
        type=comma_list,
        help='Comma-separated list of imaging types to include. Options: {}'.format(
            ', '.join(valid_imaging_types)
        ),
    )
    parser.add_argument(
        '--exclude-unverified',
        dest='include_unverified',
        action='store_false',
        help='Flag to exclude unverified images',
    )
    parser.add_argument(
        '--exclude-verified',
        dest='include_verified',
        action='store_false',
        help='Flag to exclude verified images',
    )
    parser.add_argument(
        '--min-longitude', dest='min_longitude', type=float, help='Minimum longitude'
    )
    parser.add_argument(
        '--max-longitude', dest='max_longitude', type=float, help='Maximum longitude'
    )
    parser.add_argument(
        '--min-latitude', dest='min_latitude', type=float, help='Minimum latitude'
    )
    parser.add_argument(
        '--max-latitude', dest='max_latitude', type=float, help='Maximum latitude'
    )
    parser.add_argument(
        '--min-depth', dest='min_depth', type=float, help='Minimum depth'
    )
    parser.add_argument(
        '--max-depth', dest='max_depth', type=float, help='Maximum depth'
    )
    parser.add_argument(
        '--institutions',
        dest='owner_institution_codes',
        type=comma_list,
        help='Comma-separated list of owner institution codes to include',
    )
    parser.add_argument(
        '-a',
        '--all',
        dest='all',
        action='store_true',
        help='Flag to include all bounding boxes of other concepts in specified images',
    )
    parser.add_argument(
        '--format',
        dest='format',
        type=lowercase_str,
        default='voc',
        choices=valid_dataset_formats,
        help='Dataset format. Options: {}'.format(', '.join(valid_dataset_formats)),
    )
    parser.add_argument(
        '--img-download',
        dest='img_dir',
        default=None,
        type=str,
        help='Local directory to download images',
    )

    list_or_file = parser.add_mutually_exclusive_group(required=False)
    list_or_file.add_argument(
        '-c',
        '--concepts',
        dest='concepts',
        type=comma_list,
        help='Comma-separated list of concepts to include',
    )
    list_or_file.add_argument(
        '--concepts-file',
        dest='concepts_file',
        type=str,
        help='File containing newline-delimited list of concepts to include',
    )

    count_or_output = parser.add_mutually_exclusive_group(required=True)
    count_or_output.add_argument(
        '--count',
        dest='count',
        action='store_true',
        help='Count images and bounding boxes instead of generating a dataset',
    )
    count_or_output.add_argument(
        '-o', '--output', dest='output', type=str, help='Output directory'
    )

    # Parse arguments
    args = parser.parse_args()

    # Set log level
    level = logging.WARNING
    if args.v == 1:
        level = logging.INFO
    elif args.v >= 2:
        level = logging.DEBUG

    logging.basicConfig(level=level)

    # Parse list of concepts
    concepts = []
    if args.concepts:
        concepts = args.concepts
    elif args.concepts_file:
        if os.path.isfile(args.concepts_file):
            with open(args.concepts_file, 'r') as f:
                concepts = f.read().splitlines()
            concepts = [line.strip() for line in concepts]  # remove string format

    if not concepts:
        concepts = []

    # Parse taxonomy provider, updating concepts if necessary
    taxa_provider = args.taxa
    if taxa_provider is not None:
        taxa_provider_lower = taxa_provider.lower()
        idx = [p.lower() for p in valid_taxa_providers].index(taxa_provider_lower)
        if idx < 0:
            parser.error('Invalid taxonomy provider: {}'.format(taxa_provider))
        else:
            taxa_provider = valid_taxa_providers[idx]

        # Update concepts with all descendants
        new_concepts = []
        for concept in concepts:
            logging.debug('Finding taxa for {}'.format(concept))
            concept_taxa = taxa.find_taxa(
                taxa_provider, concept
            )  # Includes the concept itself
            for new_taxa in concept_taxa:
                new_concept = new_taxa.name
                if new_concept not in new_concepts:
                    new_concepts.append(new_concept)

        logging.debug('Old concepts: {}'.format(concepts))
        logging.debug('New concepts: {}'.format(new_concepts))
        concepts = new_concepts

    # Parse contributor email
    contributor_email = args.contributor_email
    if contributor_email is not None:
        if contributor_email not in valid_contributor_emails:
            parser.error('Invalid contributor email: {}'.format(contributor_email))

    # Parse start timestamp
    start_timestamp = args.start_timestamp
    start_timestamp_str = None
    if start_timestamp is not None:
        if start_timestamp > datetime.datetime.now():
            parser.error('Start timestamp cannot be in the future')
        start_timestamp_str = start_timestamp.isoformat(timespec='milliseconds') + 'Z'

    # Parse end timestamp
    end_timestamp = args.end_timestamp
    end_timestamp_str = None
    if end_timestamp is not None:
        if end_timestamp > datetime.datetime.now():
            parser.error('End timestamp cannot be in the future')
        end_timestamp_str = end_timestamp.isoformat(timespec='milliseconds') + 'Z'

    # Parse imaging types
    imaging_types = args.imaging_types
    if imaging_types:
        for imaging_type in imaging_types:
            if imaging_type not in valid_imaging_types:
                parser.error('Invalid imaging type: {}'.format(imaging_type))

    # Parse unverified/verified flags
    include_unverified = args.include_unverified
    include_verified = args.include_verified

    # Parse longitude/latitude/depth ranges
    min_longitude = args.min_longitude
    max_longitude = args.max_longitude
    min_latitude = args.min_latitude
    max_latitude = args.max_latitude
    min_depth = args.min_depth
    max_depth = args.max_depth

    # Parse list of owner institution codes
    owner_institution_codes = args.owner_institution_codes
    if owner_institution_codes is not None:
        for owner_institution_code in owner_institution_codes:
            if owner_institution_code not in valid_owner_institution_codes:
                parser.error(
                    'Invalid owner institution code: {}'.format(owner_institution_code)
                )

    # Pack specified constraints into base constraint instance
    base_constraints = GeoImageConstraints(
        contributorsEmail=contributor_email,
        startTimestamp=start_timestamp_str,
        endTimestamp=end_timestamp_str,
        imagingTypes=imaging_types,
        includeUnverified=include_unverified,
        includeVerified=include_verified,
        minLongitude=min_longitude,
        maxLongitude=max_longitude,
        minLatitude=min_latitude,
        maxLatitude=max_latitude,
        minDepth=min_depth,
        maxDepth=max_depth,
        ownerInstitutionCodes=owner_institution_codes,
    )

    # Create output directory (if it doesn't exist)
    output = args.output  # None if --count flag is set
    if output is not None:
        if not os.path.exists(output):
            logging.info('Creating output directory {}'.format(output))
            os.makedirs(output)
        elif not os.path.isdir(output):
            parser.error(
                'Output directory {} exists and is not a directory'.format(output)
            )

    # Create image output directory (if it doesn't exist)
    img_dir = args.img_dir  # None if --img_download flag is not called
    if img_dir is not None:
        if not os.path.exists(img_dir):
            logging.info('Creating output directory {}'.format(img_dir))
            os.makedirs(img_dir)
        elif not os.path.isdir(img_dir):
            parser.error(
                'Image download output directory {} exists and is not a directory'.format(
                    img_dir
                )
            )

    logging.info('Successfully parsed flags')

    # Pack everything into an arguments instance
    return Arguments(
        output=output,
        concepts=concepts,
        base_constraints=base_constraints,
        include_all=args.all,
        format=args.format,
        img_dir=args.img_dir,
    )


def main():
    """Entry point for the script."""
    args = parse_args()  # Will exit the script on error
    try:
        dataset_images = get_images(args)  # Get the images
    except KeyboardInterrupt:
        logging.info('Image querying interrupted by user')
        exit(0)

    if not dataset_images:  # Ensure there are images to use
        exit(0)

    try:
        error = generate_dataset(args, dataset_images)  # Generate the dataset
    except KeyboardInterrupt:
        logging.info('Dataset generation interrupted by user')
        exit(0)

    if args.img_dir:
        try:
            download_imgs(
                args, dataset_images
            )  # download the images to specified output directory
        except KeyboardInterrupt:
            logging.info('Image download interrupted by user')
            exit(0)
    else:
        exit(0)

    if error:
        logging.error('Error generating dataset.')
        exit(1)
