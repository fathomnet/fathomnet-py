# firebase.py (fathomnet-py)
from typing import Optional

from .. import models
from . import EndpointManager


class Firebase(EndpointManager):
    PATH = 'firebase'


def auth() -> models.AuthHeader:
    raise NotImplementedError  # TODO figure out firebase authentication

    res_json = Firebase.post('auth',
                             json={})
    return models.AuthHeader.from_dict(res_json)


def test(auth_header: Optional[models.AuthHeader] = None) -> models.Message:
    res_json = Firebase.get('test', auth=auth_header)
    return models.Message.from_dict(res_json)
