# comments.py (fathomnet-py)

from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class Comments(EndpointManager):
    PATH = "comments"


def create(
    uuid: str,
    comment_content: dto.BoundingBoxCommentContent,
    auth_header: Optional[dto.AuthHeader] = None,
) -> dto.BoundingBoxComment:
    """Create a comment."""
    res_json = Comments.post(
        "boundingbox/{}".format(uuid), json=comment_content.to_dict(), auth=auth_header
    )
    return dto.BoundingBoxComment.from_dict(res_json)


def find_by_uuid(uuid: str) -> dto.BoundingBoxComment:
    """Get a comment by uuid."""
    res_json = Comments.get(uuid)
    return dto.BoundingBoxComment.from_dict(res_json)


def update(
    uuid: str,
    comment_content: dto.BoundingBoxCommentContent,
    auth_header: Optional[dto.AuthHeader] = None,
) -> dto.BoundingBoxComment:
    """Update a comment."""
    res_json = Comments.put(uuid, json=comment_content.to_dict(), auth=auth_header)
    return dto.BoundingBoxComment.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None) -> None:
    """Delete a comment."""
    res = Comments.delete(uuid, parse_json=False, auth=auth_header)
    return res.status_code == 200


def find_by_bounding_box_uuid(
    uuid: str, auth_header: Optional[dto.AuthHeader] = None
) -> List[dto.BoundingBoxComment]:
    """Get a list of comments by bounding box uuid."""
    res_json = Comments.get("boundingbox/{}".format(uuid), auth=auth_header)
    return list(map(dto.BoundingBoxComment.from_dict, res_json))


def find_by_email(
    email: str,
    pageable: Optional[dto.Pageable] = None,
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.BoundingBoxComment]:
    """Get a list of comments by email."""
    params = {"email": email}
    if pageable:
        params.update(pageable.to_dict())
    res_json = Comments.get("query/email", params=params, auth=auth_header)
    return list(map(dto.BoundingBoxComment.from_dict, res_json.get("content", [])))


def flag(
    uuid: str, value: bool, auth_header: Optional[dto.AuthHeader] = None
) -> dto.BoundingBoxComment:
    """Flag a comment."""
    res_json = Comments.post(
        "flag/{}".format(uuid), params={"flag": value}, auth=auth_header
    )
    return dto.BoundingBoxComment.from_dict(res_json)
