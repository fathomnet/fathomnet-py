# xapikey.py (fathomnet-py)
from typing import Optional

from fathomnet import dto
from fathomnet.api import SESSION, EndpointManager


class XApiKey(EndpointManager):
    PATH = "xapikey"


def auth(api_key: str) -> dto.AuthHeader:
    """Exchange an API key for a JWT."""
    res_json = XApiKey.post("auth", headers={"X-API-Key": api_key})
    auth_header = dto.AuthHeader.from_dict(res_json)
    SESSION.auth = auth_header  # Update session auth
    return auth_header


def index(auth_header: Optional[dto.AuthHeader] = None):
    """Test a JWT to ensure it's valid."""
    res_json = XApiKey.get("test", auth=auth_header)
    return dto.Message.from_dict(res_json)
