# tags.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class Tags(EndpointManager):
    PATH = "tags"


def create_with_dto(
    tag: dto.TagDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.TagDTO:
    """Create a tag."""
    res_json = Tags.post("", json=tag.to_dict(), auth=auth_header)
    return dto.TagDTO.from_dict(res_json)


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
    res_json = Tags.put(uuid, json=tag.to_dict(), auth=auth_header)
    return dto.TagDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None):
    """Delete a tag."""
    Tags.delete(uuid, auth=auth_header)
