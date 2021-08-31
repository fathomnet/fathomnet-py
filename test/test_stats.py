from unittest import TestCase

from fathomnet.api import stats


class TestStatsAPI(TestCase):
    def test_most_popular_searches(self):
        results = stats.most_popular_searches()
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
