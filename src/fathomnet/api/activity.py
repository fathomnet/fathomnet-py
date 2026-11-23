# activity.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager
from fathomnet.api._paging import list_result, page_params


class Activity(EndpointManager):
    PATH = "activity"


def find_all_page(
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    include_self: Optional[bool] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.Activity]:
    """Get a page of activity for the authenticated user's followed topics, newest first.

    The server always orders activity by last update; any sort in the pageable is ignored.
    """
    params = page_params(
        pageable,
        {
            "startTimestamp": start_timestamp,
            "endTimestamp": end_timestamp,
            "includeSelf": include_self,
        },
    )
    res_json = Activity.get("", params=params, auth=auth_header)
    return dto.Page[dto.Activity].from_dict(res_json)


def find_all(
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    include_self: Optional[bool] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.Activity]:
    """Get a list of activity for the authenticated user's followed topics, newest first.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: find_all_page(
            auth_header, start_timestamp, end_timestamp, include_self, p
        ),
        pageable,
        limit,
        offset,
        func_name="activity.find_all",
    )


def find_by_email_page(
    email: str,
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.Activity]:
    """Get a page of activity by email, newest first."""
    params = page_params(
        pageable, {"startTimestamp": start_timestamp, "endTimestamp": end_timestamp}
    )
    res_json = Activity.get(
        "query/email/{}".format(email), params=params, auth=auth_header
    )
    return dto.Page[dto.Activity].from_dict(res_json)


def find_by_email(
    email: str,
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.Activity]:
    """Get a list of activity by email, newest first.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: find_by_email_page(
            email, auth_header, start_timestamp, end_timestamp, p
        ),
        pageable,
        limit,
        offset,
        func_name="activity.find_by_email",
    )


def find_by_email_admin_page(
    email: str,
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    pageable: Optional[dto.Pageable] = None,
) -> dto.Page[dto.Activity]:
    """(Admin) Get a page of activity for the topics an email follows. Used to support notification applications."""
    params = page_params(
        pageable, {"startTimestamp": start_timestamp, "endTimestamp": end_timestamp}
    )
    res_json = Activity.get(
        "admin/query/email/{}".format(email), params=params, auth=auth_header
    )
    return dto.Page[dto.Activity].from_dict(res_json)


def find_by_email_admin(
    email: str,
    auth_header: Optional[dto.AuthHeader] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    pageable: Optional[dto.Pageable] = None,
) -> List[dto.Activity]:
    """(Admin) Get a list of activity for the topics an email follows. Used to support notification applications.

    Returns the server's default page size unless a pageable is given.
    ``limit``/``offset`` are deprecated in favor of ``pageable``.
    """
    return list_result(
        lambda p: find_by_email_admin_page(
            email, auth_header, start_timestamp, end_timestamp, p
        ),
        pageable,
        limit,
        offset,
        func_name="activity.find_by_email_admin",
    )
