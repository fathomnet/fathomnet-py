from unittest import TestCase

from fathomnet.api import licenses


class TestLicensesAPI(TestCase):
    def test_find_all(self):
        results = licenses.find_all()
        self.assertGreater(len(results), 0)
        self.assertIn("CC-BY-4.0", [license.spdxId for license in results])

    def test_find_by_spdx_id_or_url(self):
        license = licenses.find_by_spdx_id_or_url("CC-BY-4.0")
        self.assertEqual(license.spdxId, "CC-BY-4.0")
        self.assertIsNotNone(license.name)
