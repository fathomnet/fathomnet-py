# images.py (fathomnet-py)
from typing import List, Optional
from urllib.parse import quote_plus

from .. import models
from . import EndpointManager


class Images(EndpointManager):
    PATH = 'images'


def find_all_alt(pageable: models.Pageable) -> List[models.AImageDTO]:
    res_json = Images.get('',
                          params=pageable.to_params())
    return list(map(models.AImageDTO.from_dict, res_json['content']))


def create_if_not_exists(images: List[models.Image], auth_header: Optional[models.AuthHeader] = None) -> List[models.AImageDTO]:
    res_json = Images.post('',
                           json=list(map(models.Image.to_dict, images)),
                           auth=auth_header)
    return list(map(models.Image.from_dict, res_json))


def count_all() -> models.Count:
    res_json = Images.get('count')
    return models.Count.from_dict(res_json)


def find_all(pageable: models.Pageable) -> List[models.AImageDTO]:
    res_json = Images.get('list/all',
                          params=pageable.to_params())
    # Note: schema inconsistent with response, need to grab the 'content' object
    return list(map(models.AImageDTO.from_dict, res_json['content']))


def find_distinct_submitter() -> List[str]:
    res_json = Images.get('list/contributors')
    return res_json


def list_imaging_types() -> List[str]:
    res_json = Images.get('list/imagingtypes')
    return res_json


def find(geo_image_constraints: models.GeoImageConstraints) -> List[models.AImageDTO]:
    res_json = Images.post('query',
                           json=geo_image_constraints.to_dict())
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_concept(concept: str, taxa: Optional[str] = None) -> List[models.AImageDTO]:
    res_json = Images.get('query/concept/{}'.format(concept),
                          params={'taxa': taxa} if taxa else None)
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_contributors_email(contributors_email: str) -> List[models.AImageDTO]:
    res_json = Images.get('query/contributor/{}'.format(contributors_email))
    return list(map(models.AImageDTO.from_dict, res_json))


def count_by_submitter(contributors_email: str) -> models.ByContributorCount:
    res_json = Images.get('query/count/contributor/{}'.format(contributors_email))
    return models.ByContributorCount.from_dict(res_json)


def find_by_observer(observer: str) -> List[models.AImageDTO]:
    res_json = Images.get('query/observer/{}'.format(observer))
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_sha256(sha256: str) -> List[models.AImageDTO]:
    res_json = Images.get('query/sha256/{}'.format(sha256))
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_tag_key(key: str, value: str) -> List[models.AImageDTO]:
    res_json = Images.get('query/tags',
                          params={'key': key, 'value': value})
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_url(url: str) -> models.AImageDTO:
    res_json = Images.get('query/url/{}'.format(quote_plus(url)))
    return models.AImageDTO.from_dict(res_json)


def find_by_uuid_in_list(uuids: List[str]) -> List[models.AImageDTO]:
    res_json = Images.post('query/uuids',
                           json=uuids)
    return list(map(models.AImageDTO.from_dict, res_json))


def find_by_uuid(uuid: str) -> models.AImageDTO:
    res_json = Images.get(uuid)
    return models.AImageDTO.from_dict(res_json)


def update(uuid: str, image: models.AImageDTO, auth_header: Optional[models.AuthHeader] = None) -> models.AImageDTO:
    res_json = Images.put(uuid,
                          json=image.to_dict(),
                          auth=auth_header)
    return models.AImageDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[models.AuthHeader] = None):
    Images.delete(uuid, auth=auth_header)
