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

    def test_find_taxa_worms_species(self):
        # Regression: issue #35, the taxa endpoint 500s for non-genus ranks
        results = taxa.find_taxa("worms", "Mycteroperca microlepis")
        self.assertIsNotNone(results)
        self.assertIn("Mycteroperca microlepis", set(item.name for item in results))

    def test_find_taxa_worms_family(self):
        results = taxa.find_taxa("worms", "Serranidae")
        self.assertIsNotNone(results)
        names = set(item.name for item in results)
        self.assertIn("Serranidae", names)
        self.assertIn("Serranus", names)
        self.assertIn("Centropristis striata", names)

    def test_find_taxa_worms_genus(self):
        results = taxa.find_taxa("worms", "Nanomia")
        self.assertEqual(
            sorted((item.name, item.rank) for item in results),
            [
                ("Nanomia", "Genus"),
                ("Nanomia bijuga", "Species"),
                ("Nanomia cara", "Species"),
                ("Nanomia septata", "Species"),
            ],
        )

    def test_find_children_worms(self):
        children = taxa.find_children("worms", "Bathochordaeus")
        self.assertIsNotNone(children)
        self.assertIn("Bathochordaeus mcnutti", set(child.name for child in children))

    def test_find_parent_worms(self):
        parent = taxa.find_parent("worms", "Bathochordaeus mcnutti")
        self.assertIsNotNone(parent)
        self.assertEqual(parent.name, "Bathochordaeus")
