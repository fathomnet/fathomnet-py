# util.py (fathomnet-py)

import requests

from fathomnet.dto import Pageable


def debug_format_response(response: requests.Response) -> str:
    """
    Formats a response object into a string for debugging purposes.

    Args:
        response: The response object to format.

    Returns:
        A string representation of the response object.
    """
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


def page(f: callable, size: int, *args, **kwargs):
    """
    Calls the given function with the given arguments, and returns a generator that will yield all results, page by page, until there are no more results.

    Assumes that the given function takes a Pageable as its first argument, and that the return value of the function is a list-like object that evaluates to False when there are no more results.

    Args:
        f: The function to call
        size: The page size to use
        *args: The arguments to pass to the function
        **kwargs: The keyword arguments to pass to the function

    Returns:
        A generator that will yield all results, page by page, until there are no more results.
    """
    number = 0
    while True:
        pageable = Pageable(size=size, number=number)
        page = f(pageable, *args, **kwargs)

        if not page:
            break

        yield from page
        number += 1
