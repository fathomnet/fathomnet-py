from unittest import TestCase, SkipTest

from . import skipIfNoAuth
from fathomnet import models
from fathomnet.api import regions


class TestRegionsAPI(TestCase):
    def test_find_all(self):
        results = regions.find_all()
        self.assertIsNotNone(results)

    def test_count_all(self):
        count = regions.count_all()
        self.assertGreater(count, 0)

    def test_find_all_paged(self):
        n_regions = 10
        pageable = models.Pageable(size=n_regions)
        results = regions.find_all_paged(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_regions)

    @skipIfNoAuth
    def test_sync(self):
        raise SkipTest('Sync endpoint not yet implemented')  # TODO sync test
