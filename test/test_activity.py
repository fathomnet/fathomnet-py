from unittest import TestCase, SkipTest

from . import skipIfNoAuth
from fathomnet.api import activity


class TestActivityAPI(TestCase):
    @skipIfNoAuth
    def test_find_all(self):
        activities = activity.find_all()
        self.assertIsNotNone(activities)

    @skipIfNoAuth
    def test_find_by_email(self):
        activities = activity.find_by_email('kbarnard@mbari.org')
        self.assertIsNotNone(activities)

    @skipIfNoAuth
    def test_find_by_email_admin(self):
        raise SkipTest('Not implemented')
