# firebase.py (fathomnet-py)
from typing import Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class Firebase(EndpointManager):
    PATH = 'firebase'


def auth() -> dto.AuthHeader:
    """Authenticate via firebase and get a JWT."""
    raise NotImplementedError  # TODO figure out firebase authentication

    res_json = Firebase.post('auth',
                             json={})
    return dto.AuthHeader.from_dict(res_json)


def test(auth_header: Optional[dto.AuthHeader] = None) -> dto.Message:
    """Test an authorization token."""
    res_json = Firebase.get('test', auth=auth_header)
    return dto.Message.from_dict(res_json)
