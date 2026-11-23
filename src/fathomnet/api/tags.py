# tags.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager
from fathomnet.api._paging import page_params


class Tags(EndpointManager):
    PATH = "tags"


def create_with_dto(
    tag: dto.TagDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.TagDTO:
    """Create a tag."""
    res_json = Tags.post("", json=tag.to_dict(), auth=auth_header)
    return dto.TagDTO.from_dict(res_json)


def create_for_image(
    image_uuid: str, tag: dto.TagDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.TagDTO:
    """Create a tag on the image with the given UUID."""
    res_json = Tags.post(image_uuid, json=tag.to_dict(), auth=auth_header)
    return dto.TagDTO.from_dict(res_json)


def count_distinct() -> dto.Count:
    """Get a count of distinct tags (key, value, media type)."""
    res_json = Tags.get("count/distinct")
    return dto.Count.from_dict(res_json)


def count_distinct_keys() -> dto.Count:
    """Get a count of distinct tag keys."""
    res_json = Tags.get("count/distinct/keys")
    return dto.Count.from_dict(res_json)


def find_distinct_page(
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.SimpleTag]:
    """Get a page of distinct tags (key, value, media type)."""
    res_json = Tags.get("list/distinct", params=page_params(pageable))
    return dto.Page[dto.SimpleTag].from_dict(res_json)


def find_distinct(
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.SimpleTag]:
    """Get a paged list of distinct tags (key, value, media type) (the server's default page size unless a pageable is given)."""
    return find_distinct_page(pageable).content


def find_distinct_keys_page(
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[str]:
    """Get a page of distinct tag keys."""
    res_json = Tags.get("list/distinct/keys", params=page_params(pageable))
    return dto.Page[str].from_dict(res_json)


def find_distinct_keys(
    pageable: Optional[dto.Pageable] = None,
) -> List[str]:
    """Get a paged list of distinct tag keys (the server's default page size unless a pageable is given)."""
    return find_distinct_keys_page(pageable).content


def find_by_uuid(uuid: str) -> dto.TagDTO:
    """Get a tag by UUID."""
    res_json = Tags.get(uuid)
    return dto.TagDTO.from_dict(res_json)


def find_by_image_uuid_and_key(image_uuid: str, key: str) -> List[dto.TagDTO]:
    """Get a tag by image UUID and key."""
    res_json = Tags.get("query/bykey/{}/{}".format(image_uuid, key))
    return list(map(dto.TagDTO.from_dict, res_json))


def update(
    uuid: str, tag: dto.TagDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.TagDTO:
    """Update a tag."""
    body = tag.to_dict()
    body["uuid"] = uuid
    res_json = Tags.put("", json=body, auth=auth_header)
    return dto.TagDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None):
    """Delete a tag."""
    Tags.delete(uuid, auth=auth_header)
