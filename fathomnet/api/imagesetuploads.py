# imagesetuploads.py (fathomnet-py)
from typing import List

from .. import models
from . import EndpointManager


class ImageSetUploads(EndpointManager):
    PATH = 'imagesetuploads'


def count_all() -> models.Count:
    """Count all image set uploads."""
    res_json = ImageSetUploads.get('count')
    return models.Count.from_dict(res_json)


def find_collections(pageable: models.Pageable) -> List[models.BImageSetUploadDTO]:
    """Get a paged list of all image set uploads."""
    res_json = ImageSetUploads.get('list/all',
                                   params=pageable.to_params())
    # Note: schema inconsistent with response, need to grab the 'content' object
    return list(map(models.BImageSetUploadDTO.from_dict, res_json['content']))


def find_contributors() -> List[str]:
    """Get a list of all contributors."""
    res_json = ImageSetUploads.get('list/contributors')
    return res_json


def find_rejection_reasons() -> List[str]:
    """Get a list of all rejection reasons."""
    res_json = ImageSetUploads.get('list/rejectionreasons')
    return res_json


def find_by_contributor(contributors_email: str) -> List[models.BImageSetUploadDTO]:
    """Get a list of image set uploads by contributor."""
    res_json = ImageSetUploads.get('query/contributor/{}'.format(contributors_email))
    return list(map(models.BImageSetUploadDTO.from_dict, res_json))


def find_by_image_uuid(image_uuid: str) -> List[models.BImageSetUploadDTO]:
    """Get an image set upload by UUID."""
    res_json = ImageSetUploads.get('query/image/{}'.format(image_uuid))
    return list(map(models.BImageSetUploadDTO.from_dict, res_json))


def stats(image_set_upload_uuid: str) -> models.ImageSetUploadStats:
    """Get image set upload statistics for a corresponding image set upload UUID."""
    res_json = ImageSetUploads.get('stats/{}'.format(image_set_upload_uuid))
    return models.ImageSetUploadStats.from_dict(res_json)


def find_by_uuid(uuid: str) -> models.BImageSetUploadDTO:
    """Get an image set upload by UUID."""
    res_json = ImageSetUploads.get(uuid)
    return models.BImageSetUploadDTO.from_dict(res_json)
