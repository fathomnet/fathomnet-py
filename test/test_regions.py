from unittest import SkipTest, TestCase

from fathomnet import dto
from fathomnet.api import regions

from . import skipIfNoAuth


class TestRegionsAPI(TestCase):
    def test_find_all(self):
        results = regions.find_all()
        self.assertIsNotNone(results)

    def test_count_all(self):
        count = regions.count_all()
        self.assertGreater(count, 0)

    def test_find_all_paged(self):
        n_regions = 10
        pageable = dto.Pageable(size=n_regions)
        results = regions.find_all_paged(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_regions)

    @skipIfNoAuth
    def test_sync(self):
        raise SkipTest("Sync endpoint not yet implemented")  # TODO sync test

    def test_find_at(self):
        latitude = 35.6
        longitude = -121.3
        results = regions.find_at(latitude, longitude)
        self.assertIsNotNone(results)
        self.assertGreaterEqual(len(results), 10)
        for region in results:
            self.assertLessEqual(latitude, region.maxLatitude)
            self.assertGreaterEqual(latitude, region.minLatitude)
            self.assertLessEqual(longitude, region.maxLongitude)
            self.assertGreaterEqual(longitude, region.minLongitude)
