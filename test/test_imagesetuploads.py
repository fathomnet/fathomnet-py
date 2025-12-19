from unittest import TestCase

from fathomnet import dto
from fathomnet.api import imagesetuploads


class TestImageSetUploadsAPI(TestCase):
    def test_count_all(self):
        count = imagesetuploads.count_all()
        self.assertIsNotNone(count)
        self.assertEqual(count.objectType, "ImageSetUploadEntity")
        self.assertGreater(count.count, 0)

    def test_find_collections(self):
        n_image_sets = 3
        pageable = dto.Pageable(size=n_image_sets)
        results = imagesetuploads.find_collections(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_image_sets)

    def test_find_contributors(self):
        contributors = imagesetuploads.find_contributors()
        self.assertIsNotNone(contributors)
        self.assertIn("brian@mbari.org", contributors)

    def test_find_rejection_reasons(self):
        rejection_reasons = imagesetuploads.find_rejection_reasons()
        self.assertIsNotNone(rejection_reasons)
        # self.assertGreater(len(rejection_reasons), 0)

    def test_find_by_contributor(self):
        contributors_email = "brian@mbari.org"
        results = imagesetuploads.find_by_contributor(contributors_email)
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        for image_set in results:
            self.assertEqual(image_set.contributorsEmail, contributors_email)

    def test_find_by_image_uuid(self):
        image_uuid = "4f5265f7-31cd-490d-a807-bc350356435d"
        results = imagesetuploads.find_by_image_uuid(image_uuid)
        self.assertIsNotNone(results)

    def test_stats(self):
        image_set_upload_uuid = "9da52a10-f7db-4897-a886-2e3fbf6b9d36"
        stats = imagesetuploads.stats(image_set_upload_uuid)
        self.assertIsNotNone(stats)
        self.assertEqual(stats.imageSetUploadUuid, image_set_upload_uuid)

    def test_find_by_uuid(self):
        uuid = "9c891f7a-976b-4376-acf9-31681e1b3a15"
        image_set = imagesetuploads.find_by_uuid(uuid)
        self.assertIsNotNone(image_set)
        self.assertEqual(image_set.uuid, uuid)
