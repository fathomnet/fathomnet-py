from unittest import TestCase

from fathomnet.api import worms
from fathomnet.dto import WormsNode


def check_for_name(node: WormsNode, name: str) -> bool:
    """Recursively check if a node or one of its descendants has a given name."""

    def recurse_check(node: WormsNode) -> bool:
        if node.name == name:
            return True
        if not node.children:
            return False
        return any(recurse_check(child) for child in node.children)

    return recurse_check(node)


class TestWormsAPI(TestCase):
    def test_count_names(self):
        count = worms.count_names()
        self.assertIsNotNone(count)
        self.assertGreater(count, 0)

    def test_get_all_names(self):
        names = worms.get_all_names()
        self.assertIsNotNone(names)

    def test_get_names_by_aphia_id(self):
        names_obj = worms.get_names_by_aphia_id(2)
        self.assertIsNotNone(names_obj)
        self.assertEqual(2, names_obj.aphiaId)

    def test_get_ancestors_names(self):
        ancestors = worms.get_ancestors_names("Animalia")
        self.assertIsNotNone(ancestors)
        self.assertIn("object", ancestors)

    def test_get_children_names(self):
        children = worms.get_children_names("Bathochordaeus")
        self.assertIsNotNone(children)
        self.assertIn("Bathochordaeus charon", children)

    def test_get_descendants_names(self):
        descendants = worms.get_descendants_names("Bathochordaeus")
        self.assertIsNotNone(descendants)
        self.assertIn("Bathochordaeus charon", descendants)

        siph_all_descendants = worms.get_descendants_names(
            "Siphonophorae", accepted=False
        )
        siph_accepted_descendants = worms.get_descendants_names(
            "Siphonophorae", accepted=True
        )
        self.assertIsNotNone(siph_all_descendants)
        self.assertIsNotNone(siph_accepted_descendants)
        self.assertGreater(len(siph_all_descendants), len(siph_accepted_descendants))

        siph_all_descendants = worms.get_descendants_names(
            "Siphonophorae", accepted=False
        )
        siph_accepted_descendants = worms.get_descendants_names(
            "Siphonophorae", accepted=True
        )
        self.assertIsNotNone(siph_all_descendants)
        self.assertIsNotNone(siph_accepted_descendants)
        self.assertGreater(len(siph_all_descendants), len(siph_accepted_descendants))

    def test_get_parent_name(self):
        parent = worms.get_parent_name("Bathochordaeus charon")
        self.assertIsNotNone(parent)
        self.assertEqual("Bathochordaeus", parent)

    def test_find_names_containing(self):
        names = worms.find_names_containing("pendicula")
        self.assertIsNotNone(names)
        self.assertIn("Appendicularia", names)

    def test_find_names_by_prefix(self):
        names = worms.find_names_by_prefix("Appendicula")
        self.assertIsNotNone(names)
        self.assertIn("Appendicularia", names)

    def test_get_synonyms_for_name(self):
        synonyms = worms.get_synonyms_for_name("Appendicularia")
        self.assertIsNotNone(synonyms)
        self.assertIn("larvaceans", synonyms)

    def test_get_ancestors(self):
        root_node = worms.get_ancestors("Animalia")
        self.assertIsNotNone(root_node)
        self.assertTrue(
            check_for_name(root_node, "object"), 'No "object" node found in ancestors'
        )

    def test_get_children(self):
        children = worms.get_children("Bathochordaeus")
        self.assertIsNotNone(children)
        for child in children:
            if child.name == "Bathochordaeus charon":
                return
        self.fail('No "Bathochordaeus charon" child found')

    def test_get_descendants(self):
        taxa_node = worms.get_descendants("Bathochordaeus")
        self.assertIsNotNone(taxa_node)
        self.assertTrue(
            check_for_name(taxa_node, "Bathochordaeus charon"),
            'No "Bathochordaeus charon" descendant found',
        )

    def test_get_parent(self):
        parent = worms.get_parent("Bathochordaeus charon")
        self.assertIsNotNone(parent)
        self.assertEqual("Bathochordaeus", parent.name)

    def test_get_info(self):
        info = worms.get_info("Bathochordaeus charon")
        self.assertIsNotNone(info)
        self.assertEqual("Bathochordaeus charon", info.name)

    def test_find_taxa_by_prefix(self):
        taxa = worms.find_taxa_by_prefix("Appendicula")
        self.assertIsNotNone(taxa)
        for taxon in taxa:
            if taxon.name == "Appendicularia":
                return
        self.fail('No "Appendicularia" taxon found')
