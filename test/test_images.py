from unittest import TestCase, SkipTest

from . import skipIfNoAuth
from fathomnet import models
from fathomnet.api import images


class TestImagesAPI(TestCase):
    def test_find_all_alt(self):
        n_images = 5
        pageable = models.Pageable(size=n_images)
        results = images.find_all_alt(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_images)

    @skipIfNoAuth
    def test_create_if_not_exists(self):
        raise SkipTest('Write tests not yet implemented')  # TODO create_if_not_exists test

    def test_count_all(self):
        count = images.count_all()
        self.assertIsNotNone(count)
        self.assertEqual(count.objectType, 'Image')
        self.assertGreater(count.count, 0)

    def test_find_all(self):
        n_images = 5
        pageable = models.Pageable(size=n_images)
        results = images.find_all(pageable)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), n_images)

    def test_find_distinct_submitter(self):
        submitters = images.find_distinct_submitter()
        self.assertIsNotNone(submitters)
        self.assertIn('brian@mbari.org', submitters)

    def test_list_imaging_types(self):
        imaging_types = images.list_imaging_types()
        self.assertIsNotNone(imaging_types)
        self.assertIn(None, imaging_types)

    def test_find(self):
        geo_image_constraints = models.GeoImageConstraints(
            concept='Bathochordaeus charon',
            taxaProviderName='mbari',
            limit=10
        )
        results = images.find(geo_image_constraints)
        self.assertIsNotNone(results)
        for image in results:
            for bounding_box in image.boundingBoxes:
                if bounding_box.concept == geo_image_constraints.concept:
                    break
            else:
                self.fail()

    def test_find_by_concept(self):
        concept = 'Bathochordaeus'
        results = images.find_by_concept(concept)
        self.assertIsNotNone(results)
        for image in results:
            for bounding_box in image.boundingBoxes:
                if bounding_box.concept == concept:
                    break
            else:
                self.fail()

    def test_find_by_contributors_email(self):
        contributors_email = 'kbarnard@mbari.org'
        results = images.find_by_contributors_email(contributors_email)
        self.assertIsNotNone(results)
        for image in results:
            self.assertEqual(image.contributorsEmail, contributors_email)

    def test_count_by_submitter(self):
        contributors_email = 'brian@mbari.org'
        count = images.count_by_submitter(contributors_email)
        self.assertIsNotNone(count)
        self.assertEqual(count.contributorsEmail, contributors_email)
        self.assertGreater(count.count, 0)

    def test_find_by_observer(self):
        observer = 'kakani'
        results = images.find_by_observer(observer)
        self.assertIsNotNone(results)
        for image in results:
            for bounding_box in image.boundingBoxes:
                if bounding_box.observer == observer:
                    break
            else:
                self.fail()

    def test_find_by_sha256(self):
        sha256 = 'b572f8ca40b5af19972d8c63ac5fa4e33df215132c4c16c47b6b483ac9d07299'
        results = images.find_by_sha256(sha256)
        self.assertIsNotNone(results)
        for image in results:
            self.assertEqual(image.sha256, sha256)

    def test_find_by_tag_key(self):
        key = 'source'
        value = 'TEST'
        results = images.find_by_tag_key(key, value)
        self.assertIsNotNone(results)
        for image in results:
            for tag in image.tags:
                if tag.key == key and tag.value == value:
                    break
            else:
                self.fail()

    def test_find_by_url(self):
        url = 'https://fathomnet.org/static/m3/framegrabs/Ventana/images/3069/00_34_35_02.png'
        image = images.find_by_url(url)
        self.assertIsNotNone(image)
        self.assertEqual(image.url, url)

    def test_find_by_uuid_in_list(self):
        uuids = [
            '86a7993e-c997-44b3-9f03-043049822dce',
            'b614d4e6-a0fb-43e9-abca-d0a496564393',
            '0b8bb542-6192-4e46-b077-cbb6fe2e33f8',
            '32a784ed-5d6c-4bc3-abf7-88b4cacb097e',
            '09911749-6480-4dfe-9632-01d678c207ba'
        ]
        results = images.find_by_uuid_in_list(uuids)
        self.assertIsNotNone(results)
        self.assertSetEqual(set(image.uuid for image in results), set(uuids))

    def test_find_by_uuid(self):
        uuid = '4f5265f7-31cd-490d-a807-bc350356435d'
        image = images.find_by_uuid(uuid)
        self.assertIsNotNone(image)
        self.assertEqual(image.uuid, uuid)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest('Write tests not yet implemented')  # TODO update test

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest('Write tests not yet implemented')  # TODO delete test
