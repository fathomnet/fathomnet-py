# images.py (fathomnet-py)
from typing import List, Optional
from urllib.parse import quote, quote_plus

from fathomnet import dto
from fathomnet.api import EndpointManager


class Images(EndpointManager):
    PATH = "images"


def find_all_alt(pageable: Optional[dto.Pageable] = None) -> List[dto.AImageDTO]:
    """Get a paged list of all images. (alternative endpoint)"""
    res_json = Images.get("", params=pageable.to_params() if pageable else None)
    return list(map(dto.AImageDTO.from_dict, res_json.get("content", [])))


def create_if_not_exists(
    images: List[dto.Image], auth_header: Optional[dto.AuthHeader] = None
) -> List[dto.AImageDTO]:
    """Create an image if it doesn't exist."""
    res_json = Images.post(
        "", json=list(map(dto.Image.to_dict, images)), auth=auth_header
    )
    return list(map(dto.Image.from_dict, res_json))


def count_all() -> dto.Count:
    """Get a count of all images."""
    res_json = Images.get("count")
    return dto.Count.from_dict(res_json)


def find_all(pageable: Optional[dto.Pageable] = None) -> List[dto.AImageDTO]:
    """Get a paged list of all images."""
    res_json = Images.get("list/all", params=pageable.to_params() if pageable else None)
    # Note: schema inconsistent with response, need to grab the 'content' object
    return list(map(dto.AImageDTO.from_dict, res_json.get("content", [])))


def find_distinct_submitter() -> List[str]:
    """Get a list of all submitters."""
    res_json = Images.get("list/contributors")
    return res_json


def list_imaging_types() -> List[str]:
    """Get a list of all imaging types."""
    res_json = Images.get("list/imagingtypes")
    return res_json


def find(geo_image_constraints: dto.GeoImageConstraints) -> List[dto.AImageDTO]:
    """Get a constrained list of images."""
    res_json = Images.post("query", json=geo_image_constraints.to_dict())
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_concept(concept: str, taxa: Optional[str] = None) -> List[dto.AImageDTO]:
    """Get a list of images by concept (and optionally taxa provider)."""
    res_json = Images.get(
        "query/concept/{}".format(quote(concept)),
        params={"taxa": taxa} if taxa else None,
    )
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_contributors_email(contributors_email: str) -> List[dto.AImageDTO]:
    """Get a list of images by contributor."""
    res_json = Images.get("query/contributor/{}".format(contributors_email))
    return list(map(dto.AImageDTO.from_dict, res_json))


def count_by_submitter(contributors_email: str) -> dto.ByContributorCount:
    """Get a count of images by contributor."""
    res_json = Images.get("query/count/contributor/{}".format(contributors_email))
    return dto.ByContributorCount.from_dict(res_json)


def find_by_observer(observer: str) -> List[dto.AImageDTO]:
    """Get a list of images by observer."""
    res_json = Images.get("query/observer/{}".format(observer))
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_sha256(sha256: str) -> List[dto.AImageDTO]:
    """Get a list of images by SHA256 hash."""
    res_json = Images.get("query/sha256/{}".format(sha256))
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_tag_key(key: str, value: str) -> List[dto.AImageDTO]:
    """Get a list of images by a specified tag key-value pair."""
    res_json = Images.get("query/tags", params={"key": key, "value": value})
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_url(url: str) -> dto.AImageDTO:
    """Get an image by URL."""
    res_json = Images.get("query/url/{}".format(quote_plus(url)))
    return dto.AImageDTO.from_dict(res_json)


def find_by_uuid_in_list(uuids: List[str]) -> List[dto.AImageDTO]:
    """Get a list of images corresponding to a specified list of UUIDs."""
    res_json = Images.post("query/uuids", json=uuids)
    return list(map(dto.AImageDTO.from_dict, res_json))


def find_by_uuid(uuid: str) -> dto.AImageDTO:
    """Get an image by UUID."""
    res_json = Images.get(uuid)
    return dto.AImageDTO.from_dict(res_json)


def update(
    uuid: str, image: dto.AImageDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.AImageDTO:
    """Update an image."""
    res_json = Images.put(uuid, json=image.to_dict(), auth=auth_header)
    return dto.AImageDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None):
    """Delete an image."""
    Images.delete(uuid, auth=auth_header)
