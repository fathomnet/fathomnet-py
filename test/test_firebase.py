from unittest import SkipTest, TestCase

from fathomnet.api import firebase

from . import skipIfNoAuth


class TestFirebaseAPI(TestCase):
    def test_auth(self):
        raise SkipTest("Firebase authentication not yet implemented")

        auth_header = firebase.auth()
        self.assertIsNotNone(auth_header)
        self.assertEqual(auth_header.type, "Bearer")

    @skipIfNoAuth
    def test_test(self):
        message = firebase.test()
        self.assertIsNotNone(message)
