"""
fathomnet-generate: Generate a dataset from FathomNet localizations.
"""

import argparse
import os
import logging
import datetime
from typing import Iterable, List
from dataclasses import dataclass, replace

from ..api import images, taxa, darwincore
from ..models import AImageDTO, GeoImageConstraints

comma_list = lambda l: l.split(',')


@dataclass
class Arguments:
    """Parsed command-line arguments"""
    output_dir: str
    concepts: List[str]
    base_constraints: GeoImageConstraints


def find_images_paged(constraints: GeoImageConstraints, page_size: int = 100) -> Iterable[AImageDTO]:
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


def generate_constraints(concepts: List[str], base_constraints: GeoImageConstraints) -> Iterable[GeoImageConstraints]:
    """Generate GeoImageConstraints instances for a list of concepts from a base set of constraints"""
    for concept in concepts:
        yield replace(base_constraints, concept=concept)
        

def write_voc(image: AImageDTO, filename: str):
    """Write a single image to a file"""
    with open(filename, 'w') as f:
        f.write(image.to_pascal_voc(pretty_print=True))


def generate_voc_dataset(args: Arguments):
    """Generate a dataset (folder of Pascal VOC annotation XMLs)"""
    # Generate the GeoImageConstraints for all concepts
    all_constraints = generate_constraints(args.concepts, args.base_constraints)
    
    # Generate dict of image UUID -> image
    image_uuid_dict = {}
    for constraints in all_constraints:
        logging.info('Fetching images for concept {}'.format(constraints.concept))
        logging.debug('Constraints: {}'.format(constraints))
        concept_images = find_images_paged(constraints)
        for image in concept_images:
            image_uuid_dict[image.uuid] = image
    
    logging.info('Found {} images'.format(len(image_uuid_dict)))
    
    # Write images to output directory
    for uuid, image in image_uuid_dict.items():
        filename = '{}.{}'.format(uuid, 'xml')
        filename = os.path.join(args.output_dir, filename)
        write_voc(image, filename)


def parse_args() -> Arguments:
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description=__doc__)
    
    # Log level
    parser.add_argument(
        '-v',
        action='count',
        default=0,
        help='Increase verbosity'
    )
    
    # Output directory
    parser.add_argument(
        'output_dir',
        type=str,
        help='Output directory'
    )
    
    # Concepts (in comma-separated list)
    parser.add_argument(
        '-c', '--concepts',
        dest='concepts',
        type=comma_list,
        help='Comma-separated list of concepts to include'
    )
    
    # Taxonomy provider (for including descendants)
    valid_taxa_providers = taxa.list_taxa_providers()
    parser.add_argument(
        '-t', '--taxa',
        dest='taxa',
        type=str,
        help='Taxonomy provider (to include descendants). Options: {}'.format(', '.join(valid_taxa_providers))
    )
    
    # Contributor email
    contributor_emails = images.find_distinct_submitter()
    parser.add_argument(
        '--contributor-email',
        dest='contributor_email',
        type=str,
        help='Contributor email'
    )
    
    # Start timestamp
    parser.add_argument(
        '--start',
        dest='start_timestamp',
        type=datetime.datetime.fromisoformat,
        help='Start timestamp (formatted as ISO-8601)'
    )
    
    # End timestamp
    parser.add_argument(
        '--end',
        dest='end_timestamp',
        type=datetime.datetime.fromisoformat,
        help='End timestamp (formatted as ISO-8601)'
    )
    
    # Imaging types (as comma-separated list)
    valid_imaging_types = [t for t in images.list_imaging_types() if t is not None]
    parser.add_argument(
        '--imaging-types',
        dest='imaging_types',
        type=comma_list,
        help='Comma-separated list of imaging types to include. Options: {}'.format(', '.join(valid_imaging_types))
    )
    
    # Exclude unverified
    parser.add_argument(
        '--exclude-unverified',
        dest='include_unverified',
        action='store_false',
        help='Flag to exclude unverified images'
    )
    
    # Exclude verified
    parser.add_argument(
        '--exclude-verified',
        dest='include_verified',
        action='store_false',
        help='Flag to exclude verified images'
    )
    
    # Minimum longitude
    parser.add_argument(
        '--min-longitude',
        dest='min_longitude',
        type=float,
        help='Minimum longitude'
    )
    
    # Maximum longitude
    parser.add_argument(
        '--max-longitude',
        dest='max_longitude',
        type=float,
        help='Maximum longitude'
    )
    
    # Minimum latitude
    parser.add_argument(
        '--min-latitude',
        dest='min_latitude',
        type=float,
        help='Minimum latitude'
    )
    
    # Maximum latitude
    parser.add_argument(
        '--max-latitude',
        dest='max_latitude',
        type=float,
        help='Maximum latitude'
    )
    
    # Minimum depth
    parser.add_argument(
        '--min-depth',
        dest='min_depth',
        type=float,
        help='Minimum depth'
    )
    
    # Maximum depth
    parser.add_argument(
        '--max-depth',
        dest='max_depth',
        type=float,
        help='Maximum depth'
    )
    
    # Owner institution codes (as comma-separated list)
    valid_owner_institution_codes = darwincore.find_owner_institution_codes()
    parser.add_argument(
        '--institutions',
        dest='owner_institution_codes',
        type=comma_list,
        help='Comma-separated list of owner institution codes to include'
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
    concepts = args.concepts
    if not concepts:
        parser.error('No concepts specified')
    
    # Parse taxonomy provider
    taxa_provider = args.taxa
    if taxa_provider is not None:
        taxa_provider_lower = taxa_provider.lower()
        idx = [p.lower() for p in valid_taxa_providers].index(taxa_provider_lower)
        if idx < 0:
            parser.error('Invalid taxonomy provider: {}'.format(taxa_provider))
        else:
            taxa_provider = valid_taxa_providers[idx]
    
    # Parse contributor email
    contributor_email = args.contributor_email
    if contributor_email is not None:
        if contributor_email not in contributor_emails:
            parser.error('Invalid contributor email: {}'.format(contributor_email))
    
    # Parse start timestamp
    start_timestamp = args.start_timestamp
    start_timestamp_str = None
    if start_timestamp is not None:
        if start_timestamp > datetime.datetime.now():
            parser.error('Start timestamp cannot be in the future')
        start_timestamp_str = start_timestamp.isoformat()
    
    # Parse end timestamp
    end_timestamp = args.end_timestamp
    end_timestamp_str = None
    if end_timestamp is not None:
        if end_timestamp > datetime.datetime.now():
            parser.error('End timestamp cannot be in the future')
        end_timestamp_str = end_timestamp.isoformat()
    
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
                parser.error('Invalid owner institution code: {}'.format(owner_institution_code))
            
    # Pack specified constraints into base constraint instance
    base_constraints = GeoImageConstraints(
        taxaProviderName=taxa_provider,
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
        ownerInstitutionCodes=owner_institution_codes
    )
    
    # Create output directory (if it doesn't exist)
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        logging.info('Creating output directory {}'.format(args.output_dir))
        os.makedirs(output_dir)
    elif not os.path.isdir(output_dir):
        parser.error('Output directory {} exists and is not a directory'.format(args.output_dir))
            
    logging.info('Successfully parsed flags')
    
    # Pack everything into an arguments instance
    return Arguments(
        output_dir=output_dir,
        concepts=concepts,
        base_constraints=base_constraints
    )


def main():
    """Entry point for the script."""
    args = parse_args()  # Will gracefully exit the script on error
    
    generate_voc_dataset(args)
