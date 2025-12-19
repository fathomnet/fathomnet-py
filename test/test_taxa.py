from unittest import TestCase

from fathomnet.api import taxa


class TestTaxaAPI(TestCase):
    def test_list_taxa_providers(self):
        taxa_providers = taxa.list_taxa_providers()
        self.assertIsNotNone(taxa_providers)
        self.assertGreater(len(taxa_providers), 0)

    def test_find_children(self):
        children = taxa.find_children("fathomnet", "Bathochordaeus")
        self.assertIsNotNone(children)
        self.assertIn("Bathochordaeus mcnutti", set(child.name for child in children))

    def test_find_parent(self):
        parent = taxa.find_parent("fathomnet", "Bathochordaeus mcnutti")
        self.assertIsNotNone(parent)
        self.assertEqual(parent.name, "Bathochordaeus")

    def test_find_taxa(self):
        concept = "Bathochordaeus"
        rank = "Genus"
        results = taxa.find_taxa("fathomnet", concept)
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)
        for taxa_item in results:
            if taxa_item.name == concept and taxa_item.rank == rank:
                break
        else:
            self.fail()
