# util.py (fathomnet-download)

import requests


def debug_format_response(response: requests.Response) -> str:
    request = response.request
    formatted_str = '''REQUEST:
    Method: {}
    URL: {}
    Headers:
        {}

    Body:
    {}

RESPONSE:
    Status: {}
    Headers:
        {}
    Content:
    {}
    '''.format(
        request.method,
        request.url,
        '\n\t'.join(['{}: {}'.format(key, val) for key, val in request.headers.items()]),
        request.body,
        response.status_code,
        '\n\t'.join(['{}: {}'.format(key, val) for key, val in response.headers.items()]),
        response.content
    )

    return formatted_str
