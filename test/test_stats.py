from unittest import TestCase

from fathomnet.api import stats


class TestStatsAPI(TestCase):
    def test_most_popular_searches(self):
        results = stats.most_popular_searches()
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)

    def test_image_set_upload_positions(self):
        positions = stats.image_set_upload_positions()
        self.assertIsNotNone(positions)
        # Should return a list
        self.assertIsInstance(positions, list)
        # If there are results, verify the structure
        if len(positions) > 0:
            position = positions[0]
            self.assertIsNotNone(position.latitude)
            self.assertIsNotNone(position.longitude)
            self.assertIsNotNone(position.imageSetUploadUuid)

    def test_contribution_stats(self):
        stats_list = stats.contribution_stats()
        self.assertIsNotNone(stats_list)
        # Should return a list
        self.assertIsInstance(stats_list, list)
        # If there are results, verify the structure
        if len(stats_list) > 0:
            contribution_stat = stats_list[0]
            self.assertIsNotNone(contribution_stat.ownerInstitutionCode)
            self.assertIsNotNone(contribution_stat.totalUploads)
            self.assertIsNotNone(contribution_stat.totalImages)
