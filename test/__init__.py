from unittest import skipIf

from fathomnet.api import xapikey

# Set this to an API key in order to perform authentication and enable test cases decorated by @skipIfNoAuth
TEST_X_API_KEY = None


if (
    TEST_X_API_KEY is not None
):  # If test X-API-Key is provided, authenticate session to enable cases
    xapikey.auth(TEST_X_API_KEY)


def skipIfNoAuth(f):  # Decorator to skip test case if it needs auth
    return skipIf(
        TEST_X_API_KEY is None, "Test X-API-Key not specified. (see test/__init__.py)"
    )(f)
