from unittest import TestCase

from fathomnet.api import darwincore


class TestDarwinCoreAPI(TestCase):
    def test_index(self):
        index = darwincore.index()
        self.assertIsNotNone(index)

    def test_find_owner_institution_codes(self):
        owner_institution_codes = darwincore.find_owner_institution_codes()
        self.assertIsNotNone(owner_institution_codes)
        self.assertGreater(len(owner_institution_codes), 0)
