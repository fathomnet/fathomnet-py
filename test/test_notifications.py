from unittest import SkipTest, TestCase

from fathomnet import dto
from fathomnet.api import notifications

from . import skipIfNoAuth


class TestNotificationsAPI(TestCase):
    @skipIfNoAuth
    def test_find_mine(self):
        results = notifications.find_mine(dto.Pageable(size=5))
        self.assertIsNotNone(results)
        self.assertLessEqual(len(results), 5)

    @skipIfNoAuth
    def test_mark_read(self):
        raise SkipTest("Write tests not yet implemented")
