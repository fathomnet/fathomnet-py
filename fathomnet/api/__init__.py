# __init__.py (fathomnet-py)
from typing import Union

import requests

from fathomnet.util import debug_format_response

SESSION = requests.Session()


class EndpointManager:
    ROOT = 'http://fathomnet.org:8080'
    PATH = None

    @classmethod
    def url(cls, endpoint: str) -> str:
        if cls.PATH is None:
            raise NotImplementedError
        return '/'.join([cls.ROOT, cls.PATH, endpoint])

    @classmethod
    def request(cls, method: str, endpoint: str, parse_json: bool = True, **kwargs) -> Union[requests.Response, dict, list]:
        url = cls.url(endpoint)
        res = SESSION.request(method, url, **kwargs)
        if res.ok:  # Status code < 400
            return res.json() if parse_json else res
        elif res.status_code == 401:  # Not authorized, need to authenticate
            raise ValueError('Unauthorized: please authenticate first.')
        elif res.status_code == 403:  # Forbidden, can't access this endpoint with given authentication
            raise ValueError('Forbidden: you cannot access this resource.')
        elif res.status_code < 500:  # User error
            raise ValueError('Client error ({}), please check your usage (docs: https://fathomnet-py.rtfd.io/) or open an issue at https://github.com/fathomnet/fathomnet-py/issues/new with the details below.\n{}'.format(res.status_code, debug_format_response(res)))
        else:  # Server error, debug the response
            raise ValueError('Server error ({}), please contact the FathomNet administrators with the details below.\n\n{}'.format(res.status_code, debug_format_response(res)))

    @classmethod
    def get(cls, endpoint: str, parse_json: bool = True, **kwargs) -> Union[requests.Response, dict, list]:
        return cls.request('GET', endpoint, parse_json=parse_json, **kwargs)

    @classmethod
    def put(cls, endpoint: str, parse_json: bool = True, **kwargs) -> Union[requests.Response, dict, list]:
        return cls.request('PUT', endpoint, parse_json=parse_json, **kwargs)

    @classmethod
    def post(cls, endpoint: str, parse_json: bool = True, **kwargs) -> Union[requests.Response, dict, list]:
        return cls.request('POST', endpoint, parse_json=parse_json, **kwargs)

    @classmethod
    def delete(cls, endpoint: str, parse_json: bool = True, **kwargs) -> Union[requests.Response, dict, list]:
        return cls.request('DELETE', endpoint, parse_json=parse_json, **kwargs)
