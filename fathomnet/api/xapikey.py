# xapikey.py (fathomnet-py)
from typing import Optional

from .. import models
from . import EndpointManager, session


class XApiKey(EndpointManager):
    PATH = 'xapikey'


def auth(x_api_key_token: str) -> models.AuthHeader:
    """Exchange an X-API-key token for a JWT."""
    res_json = XApiKey.post('auth', headers={'X-API-Key': x_api_key_token})  # TODO figure out request body
    auth_header = models.AuthHeader.from_dict(res_json)
    session.auth = auth_header  # Update session auth
    return auth_header


def index(auth_header: Optional[models.AuthHeader] = None):
    """Test a JWT to ensure it's valid."""
    res_json = XApiKey.get('test', auth=auth_header)
    return models.Message.from_dict(res_json)
