# __init__.py (fathomnet-py)
from typing import Union

import requests

from ..util import debug_format_response

session = requests.Session()


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
        res = session.request(method, url, **kwargs)
        if res.ok:  # Status code < 400
            return res.json() if parse_json else res
        elif res.status_code == 401:  # Not authorized, need to authenticate
            raise ValueError('Unauthorized: please authenticate first.')
        elif res.status_code == 403:  # Forbidden, can't access this endpoint with given authentication
            raise ValueError('Forbidden: you cannot access this resource.')
        elif res.status_code < 500:  # User error
            raise ValueError('Bad request: {} {}'.format(method, url))
        else:  # Server error, debug the response
            print(debug_format_response(res))
            raise ValueError('Server error, please contact the FathomNet administrators.')

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
