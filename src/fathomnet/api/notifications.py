# notifications.py (fathomnet-py)
from typing import List, Optional
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager


class Notifications(EndpointManager):
    PATH = "notifications"


def _params(pageable: Optional[dto.Pageable], **extra) -> list:
    params = pageable.to_params() if pageable else []
    params.extend((k, v) for k, v in extra.items() if v is not None)
    return params


def create(
    notification_content: dto.NotificationContent,
    auth_header: Optional[dto.AuthHeader] = None,
) -> dto.Notification:
    """(Admin) Create a notification."""
    res_json = Notifications.post(
        "", json=notification_content.to_dict(), auth=auth_header
    )
    return dto.Notification.from_dict(res_json)


def find_mine(
    pageable: Optional[dto.Pageable] = None,
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.Notification]:
    """Get a paged list of notifications for the authenticated user."""
    res_json = Notifications.get(
        "query/email", params=_params(pageable), auth=auth_header
    )
    return list(map(dto.Notification.from_dict, res_json.get("content", [])))


def find_by_email(
    email: str,
    pageable: Optional[dto.Pageable] = None,
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.Notification]:
    """(Admin) Get a paged list of notifications for an email."""
    res_json = Notifications.get(
        "query/email/{}".format(quote(email)),
        params=_params(pageable),
        auth=auth_header,
    )
    return list(map(dto.Notification.from_dict, res_json.get("content", [])))


def find_by_email_since(
    email: str,
    since: str,
    pageable: Optional[dto.Pageable] = None,
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.Notification]:
    """(Admin) Get a paged list of notifications for an email created since a timestamp (ISO 8601 / RFC 3339)."""
    res_json = Notifications.get(
        "query/email/{}/since".format(quote(email)),
        params=_params(pageable, since=since),
        auth=auth_header,
    )
    return list(map(dto.Notification.from_dict, res_json.get("content", [])))


def find_by_email_and_topic(
    email: str,
    topic: str,
    pageable: Optional[dto.Pageable] = None,
    auth_header: Optional[dto.AuthHeader] = None,
) -> List[dto.Notification]:
    """(Admin) Get a paged list of notifications for an email and topic."""
    res_json = Notifications.get(
        "query/email/{}/topic/{}".format(quote(email), quote(topic, safe="")),
        params=_params(pageable),
        auth=auth_header,
    )
    return list(map(dto.Notification.from_dict, res_json.get("content", [])))


def find_by_uuid(
    uuid: str, auth_header: Optional[dto.AuthHeader] = None
) -> dto.Notification:
    """Get a notification by UUID."""
    res_json = Notifications.get(uuid, auth=auth_header)
    return dto.Notification.from_dict(res_json)


def mark_read(
    uuid: str, auth_header: Optional[dto.AuthHeader] = None
) -> dto.Notification:
    """Mark a notification as read."""
    res_json = Notifications.put("{}/read".format(uuid), auth=auth_header)
    return dto.Notification.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[dto.AuthHeader] = None) -> None:
    """Delete a notification by UUID."""
    Notifications.delete(uuid, parse_json=False, auth=auth_header)


def delete_by_email(email: str, auth_header: Optional[dto.AuthHeader] = None) -> None:
    """(Admin) Delete all notifications for an email."""
    Notifications.delete(
        "query/email/{}".format(quote(email)), parse_json=False, auth=auth_header
    )
