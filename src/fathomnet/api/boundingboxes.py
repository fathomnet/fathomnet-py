# boundingboxes.py (fathomnet-py)
from typing import BinaryIO, List, Optional
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager


class BoundingBoxes(EndpointManager):
    PATH = "boundingboxes"


def create_with_dto(
    bounding_box: dto.BoundingBoxDTO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.BoundingBoxDTO:
    """Create a bounding box."""
    res_json = BoundingBoxes.post("", json=bounding_box.to_dict(), auth=auth_header)
    return dto.BoundingBoxDTO.from_dict(res_json)


def count_all() -> dto.Count:
    """Get a count of all bounding boxes."""
    res_json = BoundingBoxes.get("count")
    return dto.Count.from_dict(res_json)


def find_concepts() -> List[str]:
    """Get a list of all concepts."""
    res_json = BoundingBoxes.get("list/concepts")
    return res_json


def count_total_by_concept() -> List[dto.ByConceptCount]:
    """Get a count of bounding boxes for each concept."""
    res_json = BoundingBoxes.get("list/counts")
    return list(map(dto.ByConceptCount.from_dict, res_json))


def count_total_by_observer() -> List[dto.ByObserverCount]:
    """Get a count of bounding boxes for each observer."""
    res_json = BoundingBoxes.get("list/counts/observer")
    return list(map(dto.ByObserverCount.from_dict, res_json))


def count_total_by_reviewer() -> List[dto.ByReviewerCount]:
    """Get a count of bounding boxes for each reviewer."""
    res_json = BoundingBoxes.get("list/counts/reviewer")
    return list(map(dto.ByReviewerCount.from_dict, res_json))


def find_observers() -> List[str]:
    """Get a list of all observers."""
    res_json = BoundingBoxes.get("list/observers")
    return res_json


def count_by_concept(concept: str) -> dto.ByConceptCount:
    """Get a count of bounding boxes for a concept."""
    res_json = BoundingBoxes.get("query/count/{}".format(concept))
    return dto.ByConceptCount.from_dict(res_json)


def find_by_user_defined_key(user_defined_key: str) -> List[dto.BoundingBoxDTO]:
    """Get a list of bounding boxes by a user-defined key."""
    res_json = BoundingBoxes.get("query/userdefinedkey/{}".format(user_defined_key))
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def find_all_user_defined_keys() -> List[str]:
    """Get a list of all user-defined keys."""
    res_json = BoundingBoxes.get("query/userdefinedkeys")
    return res_json


def upload_csv(
    csv_fp: BinaryIO, auth_header: Optional[dto.AuthHeader] = None
) -> dto.Message:
    """Upload a CSV of bounding boxes."""
    res_json = BoundingBoxes.post("upload/csv", files={"csv": csv_fp}, auth=auth_header)
    return dto.Message.from_dict(res_json)


def find_by_uuid(uuid: str) -> dto.BoundingBoxDTO:
    """Get a bounding box by UUID."""
    res_json = BoundingBoxes.get(uuid)
    return dto.BoundingBoxDTO.from_dict(res_json)


def update(
    uuid: str,
    bounding_box: dto.ABoundingBoxDTO,
    auth_header: Optional[dto.AuthHeader] = None,
) -> dto.BoundingBoxDTO:
    """Update a bounding box."""
    res_json = BoundingBoxes.put(uuid, json=bounding_box.to_dict(), auth=auth_header)
    return dto.BoundingBoxDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None):
    """Delete a bounding box."""
    BoundingBoxes.delete(uuid, auth=auth_header)


def audit_by_uuid(uuid: str) -> List[dto.BoundingBoxDTO]:
    """Get an audit of a bounding box by UUID."""
    res_json = BoundingBoxes.get("audit/uuid/{}".format(uuid))
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def audit_by_user_defined_key(user_defined_key: str) -> List[dto.BoundingBoxDTO]:
    """Get an audit of a bounding box by user-defined key."""
    res_json = BoundingBoxes.get("audit/userdefinedkey/{}".format(user_defined_key))
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def find_searchable_concepts() -> List[str]:
    """Get a list of searchable concepts."""
    res_json = BoundingBoxes.get("list/searchable")
    return res_json


def find_by_observer_uuid(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> List[dto.BoundingBoxDTO]:
    """Get a list of bounding boxes by observer UUID."""
    res_json = BoundingBoxes.get(
        "query/observer/{}".format(uuid),
        params=pageable.to_params() if pageable else None,
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json.get("content", [])))


def find_by_reviewer_uuid(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> List[dto.BoundingBoxDTO]:
    """Get a list of bounding boxes by reviewer UUID."""
    res_json = BoundingBoxes.get(
        "query/reviewer/{}".format(uuid),
        params=pageable.to_params() if pageable else None,
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json.get("content", [])))


def audit_by_concepts(
    concepts: List[str],
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by concepts."""
    params = {}
    if start_timestamp:
        params["startTimestamp"] = start_timestamp
    if end_timestamp:
        params["endTimestamp"] = end_timestamp
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    res_json = BoundingBoxes.get(
        "audit/concepts/{}".format(quote(",".join(concepts))), params=params
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def audit_by_reviewer(
    uuid: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by reviewer UUID."""
    params = {}
    if start_timestamp:
        params["startTimestamp"] = start_timestamp
    if end_timestamp:
        params["endTimestamp"] = end_timestamp
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    res_json = BoundingBoxes.get("audit/reviewer/{}".format(uuid), params=params)
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def audit_by_observer(
    observer: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by observer."""
    params = {}
    if start_timestamp:
        params["startTimestamp"] = start_timestamp
    if end_timestamp:
        params["endTimestamp"] = end_timestamp
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    res_json = BoundingBoxes.get(
        "audit/observer/{}".format(quote(observer)), params=params
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def bulk_rename(
    boxes: List[dto.BoundingBoxDTO],
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.BoundingBoxDTO]:
    """Bulk rename bounding boxes."""
    res_json = BoundingBoxes.put(
        "bulk/rename",
        json=[box.to_dict() for box in boxes],
        auth=auth_header,
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def bulk_review(
    boxes: List[dto.BoundingBoxDTO],
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.BoundingBoxDTO]:
    """Bulk review bounding boxes."""
    res_json = BoundingBoxes.put(
        "bulk/review",
        json=[box_review.to_dict() for box_review in boxes],
        auth=auth_header,
    )
    return list(map(dto.BoundingBoxDTO.from_dict, res_json))


def find(
    constraints: dto.BoundingBoxConstraintsDTO,
) -> List[dto.BoundingBoxDTO]:
    """Query bounding boxes by constraints."""
    res_json = BoundingBoxes.post("query", json=constraints.to_dict())
    return list(map(dto.BoundingBoxDTO.from_dict, res_json.get("content", [])))


def count(
    constraints: dto.BoundingBoxConstraintsDTO,
) -> dto.Count:
    """Count bounding boxes by constraints."""
    res_json = BoundingBoxes.post("query/count", json=constraints.to_dict())
    return dto.Count.from_dict(res_json)
