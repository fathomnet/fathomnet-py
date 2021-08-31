from unittest import TestCase

from . import skipIfNoAuth, TEST_X_API_KEY
from fathomnet.api import xapikey


class TestXAPIKeyAPI(TestCase):
    @skipIfNoAuth
    def test_auth(self):
        auth_header = xapikey.auth(TEST_X_API_KEY)
        self.assertIsNotNone(auth_header)
        self.assertEqual(auth_header.type, 'Bearer')

        message = xapikey.index(auth_header)
        self.assertIsNotNone(message)
        self.assertEqual(message.message, 'Authentication successful')
