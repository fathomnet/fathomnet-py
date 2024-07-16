from os import getenv
from unittest import skipIf

from fathomnet.api import xapikey

# Set the TEST_X_API_KEY environment variable an API key in order to perform authentication and enable test cases decorated by @skipIfNoAuth
TEST_X_API_KEY = getenv("TEST_X_API_KEY")

# If test X-API-Key is provided, authenticate session to enable cases
if TEST_X_API_KEY is not None:
    xapikey.auth(TEST_X_API_KEY)


def skipIfNoAuth(f: callable) -> callable:
    """
    Decorator to skip test case if it needs auth.

    Args:
        f (callable): Test case function.

    Returns:
        callable: Test case function
    """
    return skipIf(
        TEST_X_API_KEY is None,
        "TEST_X_API_KEY environment variable not specified",
    )(f)
