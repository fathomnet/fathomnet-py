from unittest import TestCase

from fathomnet.api import darwincore


class TestDarwinCoreAPI(TestCase):
    def test_find_owner_institution_codes(self):
        owner_institution_codes = darwincore.find_owner_institution_codes()
        self.assertIsNotNone(owner_institution_codes)
        self.assertGreater(len(owner_institution_codes), 0)

    def test_find_owner_institutions_by_image_uuid(self):
        owner_institutions = darwincore.find_owner_institutions_by_image_uuid(
            "b7736c31-0b78-4761-840c-e3781d6845be"
        )
        self.assertIsNotNone(owner_institutions)
        self.assertIn("MBARI", owner_institutions)

    def test_find_by_dataset_id(self):
        dataset_id = "9596e315-82e5-407f-853d-979bd5700d43"
        darwin_core = darwincore.find_by_dataset_id(dataset_id)
        self.assertEqual(darwin_core.datasetID, dataset_id)
