# users.py (fathomnet-py)
from typing import List, Optional

from .. import models
from . import EndpointManager


class Users(EndpointManager):
    PATH = 'users'


def find_all(pageable: Optional[models.Pageable] = None, auth_header: Optional[models.AuthHeader] = None) -> List[models.FathomnetIdentity]:
    """Get a paged list of all users."""
    res_json = Users.get('', params=pageable.to_params(), auth=auth_header)
    return list(map(models.FathomnetIdentity.from_dict, res_json))


def update_user_data(fathomnet_id_mutation: models.FathomnetIdMutation, auth_header: Optional[models.AuthHeader] = None) -> models.FathomnetIdentity:
    """Update a user's account data."""
    res_json = Users.put('', json=fathomnet_id_mutation.to_dict(), auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def update_user_data_admin(uuid: str, fathomnet_id_admin_mutation: models.FathomnetIdAdminMutation, auth_header: Optional[models.AuthHeader] = None) -> models.FathomnetIdentity:
    """(Admin) Update a user's account data."""
    res_json = Users.put('admin/{}'.format(uuid), json=fathomnet_id_admin_mutation.to_dict(), auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def get_api_key(auth_header: Optional[models.AuthHeader] = None) -> models.ApiKey:
    """Get a user's API key."""
    res_json = Users.get('apikey', auth=auth_header)
    return models.ApiKey.from_dict(res_json)


def create_new_api_key(auth_header: Optional[models.AuthHeader] = None) -> models.ApiKey:
    """Create a new API key for a user."""
    res_json = Users.post('apikey', json=None, auth=auth_header)
    return models.ApiKey.from_dict(res_json)


def delete_api_key(auth_header: Optional[models.AuthHeader] = None):
    """Delete a user's API key."""
    Users.delete('apikey', auth=auth_header)


def count_all() -> models.Count:
    """Get a count of all users."""
    res_json = Users.get('count')
    return models.Count.from_dict(res_json)


def disable_by_uuid(uuid: str, auth_header: Optional[models.AuthHeader] = None):
    """(Admin) Disable an account by its UUID."""
    res_json = Users.put('disable/{}'.format(uuid), auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def find_expertise() -> List[str]:
    """Get a list of all expertise levels."""
    res_json = Users.get('list/expertise')
    return res_json


def find_contributors_names() -> List[str]:
    """Get a list of all contributor names."""
    res_json = Users.get('list/names')
    return res_json


def find_roles() -> List[str]:
    """Get a list of all user roles."""
    res_json = Users.get('list/roles')
    return res_json


def find_by_authentication(auth_header: Optional[models.AuthHeader] = None) -> models.FathomnetIdentity:
    """Find a user by authentication."""
    res_json = Users.get('query', auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def find_by_email(email: str, auth_header: Optional[models.AuthHeader] = None) -> models.FathomnetIdentity:
    """Find a user by email."""
    res_json = Users.get('query/email/{}'.format(email), auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def find_by_firebase_uid(uid: str, auth_header: Optional[models.AuthHeader] = None) -> models.FathomnetIdentity:
    """Find a user by Firebase UID."""
    res_json = Users.get('query/uid/{}'.format(uid), auth=auth_header)
    return models.FathomnetIdentity.from_dict(res_json)


def verify(auth_header: Optional[models.AuthHeader] = None) -> models.Authentication:
    """Get the contents of an authorization token."""
    res_json = Users.get('verification', auth=auth_header)
    return models.Authentication.from_dict(res_json)
