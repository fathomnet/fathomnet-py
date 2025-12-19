from unittest import SkipTest, TestCase

from fathomnet import dto
from fathomnet.api import images

from . import skipIfNoAuth


class TestImagesAPI(TestCase):
    def test_find_all_alt(self):
        n_images = 5
        pageable = dto.Pageable(size=n_images)
        results = images.find_all_alt(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_images)

    @skipIfNoAuth
    def test_create_if_not_exists(self):
        raise SkipTest(
            "Write tests not yet implemented"
        )  # TODO create_if_not_exists test

    def test_count_all(self):
        count = images.count_all()
        self.assertIsNotNone(count)
        self.assertEqual(count.objectType, "ImageEntity")
        self.assertGreater(count.count, 0)

    def test_find_all(self):
        n_images = 5
        pageable = dto.Pageable(size=n_images)
        results = images.find_all(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_images)

    def test_find_distinct_submitter(self):
        submitters = images.find_distinct_submitter()
        self.assertIsNotNone(submitters)
        self.assertIn("brian@mbari.org", submitters)

    def test_list_imaging_types(self):
        imaging_types = images.list_imaging_types()
        self.assertIsNotNone(imaging_types)
        self.assertIn("ROV", imaging_types)

    def test_find(self):
        geo_image_constraints = dto.GeoImageConstraints(
            concept="Bathochordaeus charon", taxaProviderName="fathomnet", limit=10
        )
        results = images.find(geo_image_constraints)
        self.assertIsNotNone(results)
        for image in results:
            for bounding_box in image.boundingBoxes:
                if bounding_box.concept == geo_image_constraints.concept:
                    break
            else:
                self.fail()

    # def test_find_by_concept(self):
    #     for concept in (
    #         "Bathochordaeus",
    #         "a'a",
    #         "Abraliopsis (Boreabrealiopsis) felis",
    #     ):
    #         results = images.find_by_concept(concept)
    #         self.assertIsNotNone(results)
    #         for image in results:
    #             for bounding_box in image.boundingBoxes:
    #                 if bounding_box.concept == concept:
    #                     break
    #             else:
    #                 self.fail()

    def test_find_by_contributors_email(self):
        contributors_email = "kbarnard@mbari.org"
        results = images.find_by_contributors_email(contributors_email)
        self.assertIsNotNone(results)
        for image in results:
            self.assertEqual(image.contributorsEmail, contributors_email)

    def test_count_by_submitter(self):
        contributors_email = "brian@mbari.org"
        count = images.count_by_submitter(contributors_email)
        self.assertIsNotNone(count)
        self.assertEqual(count.contributorsEmail, contributors_email)
        self.assertGreater(count.count, 0)

    def test_find_by_observer(self):
        observer = "kakani"
        results = images.find_by_observer(observer)
        self.assertIsNotNone(results)
        for image in results:
            for bounding_box in image.boundingBoxes:
                if bounding_box.observer == observer:
                    break
            else:
                self.fail()

    def test_find_by_sha256(self):
        sha256 = "b572f8ca40b5af19972d8c63ac5fa4e33df215132c4c16c47b6b483ac9d07299"
        results = images.find_by_sha256(sha256)
        self.assertIsNotNone(results)
        for image in results:
            self.assertEqual(image.sha256, sha256)

    def test_find_by_tag_key(self):
        key = "source"
        value = "TEST"
        results = images.find_by_tag_key(key, value)
        self.assertIsNotNone(results)
        for image in results:
            for tag in image.tags:
                if tag.key == key and tag.value == value:
                    break
            else:
                self.fail()

    # def test_find_by_url(self):
    #     url = "https://database.fathomnet.org/static/m3/framegrabs/Ventana/images/3069/00_34_35_02.png"
    #     image = images.find_by_url(url)
    #     self.assertIsNotNone(image)
    #     self.assertEqual(image.url, url)

    def test_find_by_uuid_in_list(self):
        uuids = [
            "b7736c31-0b78-4761-840c-e3781d6845be",
            "9b0bc09b-85b2-4b72-99db-bf91b36a9f89",
            "8bf45f3c-4d11-418c-b384-2dfdc2e6c01c",
            "bfa62293-1723-4643-8954-a60786f10ad5",
            "a1b4d4ff-a22c-417b-921f-a1dd98c21f7a",
        ]
        results = images.find_by_uuid_in_list(uuids)
        self.assertIsNotNone(results)
        self.assertSetEqual(set(image.uuid for image in results), set(uuids))

    def test_find_by_uuid(self):
        uuid = "b7736c31-0b78-4761-840c-e3781d6845be"
        image = images.find_by_uuid(uuid)
        self.assertIsNotNone(image)
        self.assertEqual(image.uuid, uuid)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest("Write tests not yet implemented")  # TODO update test

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest("Write tests not yet implemented")  # TODO delete test
