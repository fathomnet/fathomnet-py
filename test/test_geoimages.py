from unittest import TestCase

from fathomnet import dto
from fathomnet.api import geoimages


class TestGeoImagesAPI(TestCase):
    def test_find_all(self):
        n_images = 5
        pageable = dto.Pageable(size=n_images)
        results = geoimages.find_all(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_images)

    def test_count(self):
        geo_image_constraints = dto.GeoImageConstraints(
            concept="Bathochordaeus", limit=10
        )
        count = geoimages.count(geo_image_constraints)
        self.assertIsNotNone(count)
        self.assertGreater(count.count, 0)

    def test_find(self):
        geo_image_constraints = dto.GeoImageConstraints(
            concept="Bathochordaeus", limit=10
        )
        results = geoimages.find(geo_image_constraints)
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)

    def test_find_by_image_set_upload_uuid(self):
        image_set_upload_uuid = "9c891f7a-976b-4376-acf9-31681e1b3a15"
        results = geoimages.find_by_image_set_upload_uuid(image_set_upload_uuid)
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
