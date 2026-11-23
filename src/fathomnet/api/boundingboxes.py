# boundingboxes.py (fathomnet-py)
import json
from typing import Any, BinaryIO, Dict, List, Optional, Union
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager
from fathomnet.api._paging import list_result, page_params


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


def find_concepts_page(pageable: Optional[dto.Pageable] = None) -> dto.Page[str]:
    """Get a page of concepts."""
    res_json = BoundingBoxes.get("list/concepts", params=page_params(pageable))
    return dto.Page[str].from_dict(res_json)


def find_concepts(pageable: Optional[dto.Pageable] = None) -> List[str]:
    """Get a list of concepts. Returns all of them unless a pageable is given."""
    return list_result(find_concepts_page, pageable, all_pages=True)


def count_total_by_concept_page(
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.ByConceptCount]:
    """Get a page of bounding box counts by concept."""
    res_json = BoundingBoxes.get("list/counts", params=page_params(pageable))
    return dto.Page[dto.ByConceptCount].from_dict(res_json)


def count_total_by_concept(
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.ByConceptCount]:
    """Get a list of bounding box counts by concept. Returns all of them unless a pageable is given."""
    return list_result(count_total_by_concept_page, pageable, all_pages=True)


def count_total_by_observer_page(
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.ByObserverCount]:
    """Get a page of bounding box counts by observer."""
    res_json = BoundingBoxes.get("list/counts/observer", params=page_params(pageable))
    return dto.Page[dto.ByObserverCount].from_dict(res_json)


def count_total_by_observer(
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.ByObserverCount]:
    """Get a list of bounding box counts by observer. Returns all of them unless a pageable is given."""
    return list_result(count_total_by_observer_page, pageable, all_pages=True)


def count_total_by_reviewer_page(
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.ByReviewerCount]:
    """Get a page of bounding box counts by reviewer."""
    res_json = BoundingBoxes.get("list/counts/reviewer", params=page_params(pageable))
    return dto.Page[dto.ByReviewerCount].from_dict(res_json)


def count_total_by_reviewer(
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.ByReviewerCount]:
    """Get a list of bounding box counts by reviewer. Returns all of them unless a pageable is given."""
    return list_result(count_total_by_reviewer_page, pageable, all_pages=True)


def find_observers_page(pageable: Optional[dto.Pageable] = None) -> dto.Page[str]:
    """Get a page of observers."""
    res_json = BoundingBoxes.get("list/observers", params=page_params(pageable))
    return dto.Page[str].from_dict(res_json)


def find_observers(pageable: Optional[dto.Pageable] = None) -> List[str]:
    """Get a list of observers. Returns all of them unless a pageable is given."""
    return list_result(find_observers_page, pageable, all_pages=True)


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
    csv_fp: BinaryIO,
    auth_header: Optional[dto.AuthHeader] = None,
    darwin_core: Optional[Union[dto.BDarwinCore, Dict[str, Any]]] = None,
    use_contributors_email: Optional[bool] = None,
) -> dto.Message:
    """Upload a CSV of bounding boxes with its Darwin Core metadata.

    :param csv_fp: Open binary file handle of the CSV
    :param auth_header: Authorization header, defaults to the session's authentication
    :param darwin_core: Darwin Core metadata for the upload. The server rejects uploads without it.
    :param use_contributors_email: (Admin only) Attribute the upload to the Darwin Core ``contributorsEmail`` rather than the authenticated user
    """
    files = {"file": csv_fp}
    if darwin_core is not None:
        if isinstance(darwin_core, dto.DTO):
            darwin_core = darwin_core.model_dump(mode="json", exclude_none=True)
        files["darwincore"] = (
            "darwincore.json",
            json.dumps(darwin_core),
            "application/json",
        )
    params = (
        {"usecontributorsemail": use_contributors_email}
        if use_contributors_email is not None
        else None
    )
    res_json = BoundingBoxes.post(
        "upload/csv", files=files, params=params, auth=auth_header
    )
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


def find_by_observer_uuid_page(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> dto.Page[dto.BoundingBoxDTO]:
    """Get a page of bounding boxes by observer UUID."""
    res_json = BoundingBoxes.get(
        "query/observer/{}".format(uuid), params=page_params(pageable)
    )
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def find_by_observer_uuid(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> List[dto.BoundingBoxDTO]:
    """Get a list of bounding boxes by observer UUID (the server's default page size unless a pageable is given)."""
    return find_by_observer_uuid_page(uuid, pageable).content


def find_by_reviewer_uuid_page(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> dto.Page[dto.BoundingBoxDTO]:
    """Get a page of bounding boxes by reviewer UUID."""
    res_json = BoundingBoxes.get(
        "query/reviewer/{}".format(uuid), params=page_params(pageable)
    )
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def find_by_reviewer_uuid(
    uuid: str, pageable: Optional[dto.Pageable] = None
) -> List[dto.BoundingBoxDTO]:
    """Get a list of bounding boxes by reviewer UUID (the server's default page size unless a pageable is given)."""
    return find_by_reviewer_uuid_page(uuid, pageable).content


def audit_by_concepts_page(
    concepts: List[str],
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.BoundingBoxDTO]:
    """Get a page of the bounding box audit by concepts."""
    res_json = BoundingBoxes.get(
        "audit/concepts/{}".format(quote(",".join(concepts))),
        params=page_params(
            pageable,
            {"startTimestamp": start_timestamp, "endTimestamp": end_timestamp},
        ),
    )
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def audit_by_concepts(
    concepts: List[str],
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by concepts.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: audit_by_concepts_page(concepts, start_timestamp, end_timestamp, p),
        pageable,
        limit,
        offset,
        func_name="boundingboxes.audit_by_concepts",
    )


def audit_by_reviewer_page(
    uuid: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.BoundingBoxDTO]:
    """Get a page of the bounding box audit by reviewer UUID."""
    res_json = BoundingBoxes.get(
        "audit/reviewer/{}".format(uuid),
        params=page_params(
            pageable,
            {"startTimestamp": start_timestamp, "endTimestamp": end_timestamp},
        ),
    )
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def audit_by_reviewer(
    uuid: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by reviewer UUID.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: audit_by_reviewer_page(uuid, start_timestamp, end_timestamp, p),
        pageable,
        limit,
        offset,
        func_name="boundingboxes.audit_by_reviewer",
    )


def audit_by_observer_page(
    observer: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.BoundingBoxDTO]:
    """Get a page of the bounding box audit by observer."""
    res_json = BoundingBoxes.get(
        "audit/observer/{}".format(quote(observer)),
        params=page_params(
            pageable,
            {"startTimestamp": start_timestamp, "endTimestamp": end_timestamp},
        ),
    )
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def audit_by_observer(
    observer: str,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.BoundingBoxDTO]:
    """Get an audit of bounding boxes by observer.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: audit_by_observer_page(observer, start_timestamp, end_timestamp, p),
        pageable,
        limit,
        offset,
        func_name="boundingboxes.audit_by_observer",
    )


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


def find_page(
    constraints: dto.BoundingBoxConstraintsDTO,
) -> dto.Page[dto.BoundingBoxDTO]:
    """Query a page of bounding boxes by constraints. Page with ``pageNumber``/``pageSize`` on the constraints."""
    res_json = BoundingBoxes.post("query", json=constraints.to_dict())
    return dto.Page[dto.BoundingBoxDTO].from_dict(res_json)


def find(
    constraints: dto.BoundingBoxConstraintsDTO,
) -> List[dto.BoundingBoxDTO]:
    """Query bounding boxes by constraints. Returns a single page (``pageNumber``/``pageSize`` on the constraints)."""
    return find_page(constraints).content


def count(
    constraints: dto.BoundingBoxConstraintsDTO,
) -> dto.Count:
    """Count bounding boxes by constraints."""
    res_json = BoundingBoxes.post("query/count", json=constraints.to_dict())
    return dto.Count.from_dict(res_json)
