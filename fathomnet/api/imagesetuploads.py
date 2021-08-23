# imagesetuploads.py (fathomnet-py)
from typing import List

from .. import models
from . import EndpointManager


class ImageSetUploads(EndpointManager):
    PATH = 'imagesetuploads'


def count_all() -> models.Count:
    res_json = ImageSetUploads.get('count')
    return models.Count.from_dict(res_json)


def find_collections(pageable: models.Pageable) -> List[models.CImageSetUploadDTO]:
    res_json = ImageSetUploads.get('list/all',
                                   params=pageable.to_params())
    # Note: schema inconsistent with response, need to grab the 'content' object
    return list(map(models.CImageSetUploadDTO.from_dict, res_json['content']))


def find_contributors() -> List[str]:
    res_json = ImageSetUploads.get('list/contributors')
    return res_json


def find_rejection_reasons() -> List[str]:
    res_json = ImageSetUploads.get('list/rejectionreasons')
    return res_json


def find_by_contributor(contributors_email: str) -> List[models.CImageSetUploadDTO]:
    res_json = ImageSetUploads.get('query/contributor/{}'.format(contributors_email))
    return list(map(models.CImageSetUploadDTO.from_dict, res_json))


def find_by_image_uuid(image_uuid: str) -> List[models.CImageSetUploadDTO]:
    res_json = ImageSetUploads.get('query/image/{}'.format(image_uuid))
    return list(map(models.CImageSetUploadDTO.from_dict, res_json))


def stats(image_set_upload_uuid: str) -> models.ImageSetUploadStats:
    res_json = ImageSetUploads.get('stats/{}'.format(image_set_upload_uuid))
    return models.ImageSetUploadStats.from_dict(res_json)


def find_by_uuid(uuid: str) -> models.CImageSetUploadDTO:
    res_json = ImageSetUploads.get(uuid)
    return models.CImageSetUploadDTO.from_dict(res_json)
