# activity.py (fathomnet-py)

from typing import List, Optional

from fathomnet.api import EndpointManager
from fathomnet import dto


class Activity(EndpointManager):
    PATH = 'activity'


def find_all(auth_header: Optional[dto.AuthHeader] = None,
             start_timestamp: Optional[str] = None, end_timestamp: Optional[str] = None,
             limit: Optional[int] = None, offset: Optional[int] = None,
             include_self: Optional[bool] = None) -> List[dto.Activity]:
    """Get a list of all activity."""
    params = {}
    if start_timestamp:
        params['startTimestamp'] = start_timestamp
    if end_timestamp:
        params['endTimestamp'] = end_timestamp
    if limit:
        params['limit'] = limit
    if offset:
        params['offset'] = offset
    if include_self:
        params['includeSelf'] = include_self
    res_json = Activity.get('', params=params, auth=auth_header)
    return list(map(dto.Activity.from_dict, res_json))


def find_by_email(email: str,
                  auth_header: Optional[dto.AuthHeader] = None,
                  start_timestamp: Optional[str] = None, end_timestamp: Optional[str] = None,
                  limit: Optional[int] = None, offset: Optional[int] = None) -> List[dto.Activity]:
    """Get a list of activity by email."""
    params = {}
    if start_timestamp:
        params['startTimestamp'] = start_timestamp
    if end_timestamp:
        params['endTimestamp'] = end_timestamp
    if limit:
        params['limit'] = limit
    if offset:
        params['offset'] = offset
    res_json = Activity.get('query/email/{}'.format(email), params=params, auth=auth_header)
    return list(map(dto.Activity.from_dict, res_json))


def find_by_email_admin(email: str,
                        auth_header: Optional[dto.AuthHeader] = None,
                        start_timestamp: Optional[str] = None, end_timestamp: Optional[str] = None,
                        limit: Optional[int] = None, offset: Optional[int] = None) -> List[dto.Activity]:
    """(Admin) Get a list of activity by email. Used to support notification applications."""
    params = {}
    if start_timestamp:
        params['startTimestamp'] = start_timestamp
    if end_timestamp:
        params['endTimestamp'] = end_timestamp
    if limit:
        params['limit'] = limit
    if offset:
        params['offset'] = offset
    res_json = Activity.get('admin/query/email/{}'.format(email), params=params, auth=auth_header)
    return list(map(dto.Activity.from_dict, res_json))
