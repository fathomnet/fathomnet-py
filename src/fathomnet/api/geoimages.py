# geoimages.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager
from fathomnet.api._paging import MAX_PAGE_SIZE, fetch_all, list_result, page_params


class GeoImages(EndpointManager):
    PATH = "geoimages"


def find_all_page(pageable: Optional[dto.Pageable] = None) -> dto.Page[dto.GeoImage]:
    """Get a page of all geo images."""
    res_json = GeoImages.get("", params=page_params(pageable))
    return dto.Page[dto.GeoImage].from_dict(res_json)


def find_all(pageable: Optional[dto.Pageable] = None) -> List[dto.GeoImage]:
    """Get a paged list of all geo images (the server's default page size unless a pageable is given)."""
    return find_all_page(pageable).content


def count(
    geo_image_constraints: dto.GeoImageConstraints,
) -> dto.GeoImageConstraintsCount:
    """Get a constrained count of geo images."""
    res_json = GeoImages.post("count", json=geo_image_constraints.to_dict())
    return dto.GeoImageConstraintsCount.from_dict(res_json)


def find_page(
    geo_image_constraints: dto.GeoImageConstraints,
) -> dto.Page[dto.GeoImage]:
    """Get a constrained page of geo images.

    Page with ``pageNumber``/``pageSize`` (or ``limit``/``offset``) on the constraints. The page size is capped by the server.
    """
    res_json = GeoImages.post("query/paged", json=geo_image_constraints.to_dict())
    return dto.Page[dto.GeoImage].from_dict(res_json)


def find(geo_image_constraints: dto.GeoImageConstraints) -> List[dto.GeoImage]:
    """Get a constrained list of geo images.

    If the constraints set any of ``limit``, ``offset``, ``pageNumber``, or ``pageSize``, a single page is returned.
    Otherwise every matching geo image is returned, fetched page by page.
    """
    c = geo_image_constraints
    if any(v is not None for v in (c.limit, c.offset, c.pageNumber, c.pageSize)):
        return find_page(c).content
    return fetch_all(
        lambda p: find_page(
            c.model_copy(update={"pageNumber": p.number, "pageSize": p.size})
        ),
        size=MAX_PAGE_SIZE,
    )


def find_by_image_set_upload_uuid_page(
    image_set_upload_uuid: str,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.GeoImage]:
    """Get a page of geo images corresponding to an image set upload UUID."""
    res_json = GeoImages.get(
        "query/imagesetupload/{}".format(image_set_upload_uuid),
        params=page_params(pageable),
    )
    return dto.Page[dto.GeoImage].from_dict(res_json)


def find_by_image_set_upload_uuid(
    image_set_upload_uuid: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.GeoImage]:
    """Get a list of geo images corresponding to an image set upload UUID.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: find_by_image_set_upload_uuid_page(image_set_upload_uuid, p),
        pageable,
        limit,
        offset,
        func_name="geoimages.find_by_image_set_upload_uuid",
    )


def count_valid(ok: bool = True) -> dto.Count:
    """Get a count of geo images whose URL is valid (``ok=True``) or invalid (``ok=False``)."""
    res_json = GeoImages.get("count/valid", params={"ok": ok})
    return dto.Count.from_dict(res_json)


def find_valid_page(
    ok: bool = True, pageable: Optional[dto.Pageable] = None
) -> dto.Page[dto.GeoImage]:
    """Get a page of geo images whose URL is valid (``ok=True``) or invalid (``ok=False``)."""
    res_json = GeoImages.get("query/valid", params=page_params(pageable, {"ok": ok}))
    return dto.Page[dto.GeoImage].from_dict(res_json)


def find_valid(
    ok: bool = True, pageable: Optional[dto.Pageable] = None
) -> List[dto.GeoImage]:
    """Get a paged list of geo images whose URL is valid (``ok=True``) or invalid (``ok=False``)."""
    return find_valid_page(ok, pageable).content
