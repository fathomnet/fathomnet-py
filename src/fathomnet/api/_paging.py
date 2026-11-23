# _paging.py (fathomnet-py)
"""Internal helpers for paged FathomNet REST API endpoints."""

import warnings
from typing import Callable, List, Optional, TypeVar

from fathomnet import dto

T = TypeVar("T")

#: Largest page size the server will honor; larger requests are capped to this.
MAX_PAGE_SIZE = 10000

PageFn = Callable[[Optional[dto.Pageable]], "dto.Page"]


def page_params(
    pageable: Optional[dto.Pageable], params: Optional[dict] = None
) -> list:
    """Build a request parameter list from extra (non-None) parameters and a pageable."""
    out = [(k, v) for k, v in (params or {}).items() if v is not None]
    if pageable is not None:
        out.extend(pageable.to_params())
    return out


def fetch_all(page_fn: PageFn, size: int = MAX_PAGE_SIZE) -> list:
    """Fetch every page from a page function and return the concatenated content."""
    items = []
    number = 0
    while True:
        page = page_fn(dto.Pageable(size=size, number=number))
        items.extend(page.content)
        number += 1
        if not page.content or page.is_last:
            return items


def fetch_range(page_fn: PageFn, limit: int, offset: int) -> list:
    """Fetch exactly the items in [offset, offset + limit) using page-based requests."""
    if limit <= 0:
        return []
    size = min(limit, MAX_PAGE_SIZE)
    number, skip = divmod(offset, size)
    items = []
    while len(items) < limit:
        page = page_fn(dto.Pageable(size=size, number=number))
        items.extend(page.content[skip:])
        skip = 0
        number += 1
        if len(page.content) < size or (
            page.totalPages is not None and number >= page.totalPages
        ):
            break
    return items[:limit]


def list_result(
    page_fn: PageFn,
    pageable: Optional[dto.Pageable] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    default_limit: int = 100,
    all_pages: bool = False,
    func_name: str = "This function",
) -> List[T]:
    """
    Resolve a list-returning call against a paged endpoint.

    - ``limit``/``offset`` (deprecated) are translated into page requests, returning exactly that range.
    - A ``pageable`` returns that single page's content.
    - Otherwise, either every page (``all_pages=True``) or the server's default first page is returned.
    """
    if limit is not None or offset is not None:
        if pageable is not None:
            raise ValueError("Specify either pageable or limit/offset, not both.")
        warnings.warn(
            "{}: limit/offset are deprecated; pass a dto.Pageable (size, number) instead.".format(
                func_name
            ),
            DeprecationWarning,
            stacklevel=3,
        )
        return fetch_range(
            page_fn,
            limit if limit is not None else default_limit,
            offset or 0,
        )
    if pageable is not None:
        return page_fn(pageable).content
    if all_pages:
        return fetch_all(page_fn)
    return page_fn(None).content
