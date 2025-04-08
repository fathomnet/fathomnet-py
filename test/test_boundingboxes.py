from unittest import SkipTest, TestCase

from fathomnet.api import boundingboxes

from . import skipIfNoAuth


class TestBoundingBoxesAPI(TestCase):
    @skipIfNoAuth
    def test_create_with_dto(self):
        raise SkipTest("Write tests not yet implemented")  # TODO create_with_dto test

    def test_count_all(self):
        count = boundingboxes.count_all()
        self.assertIsNotNone(count)
        self.assertEqual(count.objectType, "BoundingBoxEntity")
        self.assertGreater(count.count, 0)

    def test_find_concepts(self):
        concepts = boundingboxes.find_concepts()
        self.assertIsNotNone(concepts)
        self.assertIn("Bathochordaeus", concepts)

    def test_count_total_by_concept(self):
        concept_counts = boundingboxes.count_total_by_concept()
        self.assertIsNotNone(concept_counts)
        for concept_count in concept_counts:
            if concept_count.concept == "Bathochordaeus":
                self.assertGreater(concept_count.count, 0)
                break
        else:
            self.fail()

    def test_find_observers(self):
        observers = boundingboxes.find_observers()
        self.assertIsNotNone(observers)
        self.assertIn("kakani", observers)

    def test_count_by_concept(self):
        concept_count = boundingboxes.count_by_concept("Bathochordaeus")
        self.assertIsNotNone(concept_count)
        self.assertEqual(concept_count.concept, "Bathochordaeus")
        self.assertGreater(concept_count.count, 0)

    def test_find_by_user_defined_key(self):
        user_defined_key = "00005716-ef67-44b9-0967-27ced2aab21e"
        boxes = boundingboxes.find_by_user_defined_key(user_defined_key)
        self.assertIsNotNone(boxes)
        self.assertEqual(boxes[0].userDefinedKey, user_defined_key)

    def test_find_all_user_defined_keys(self):
        user_defined_keys = boundingboxes.find_all_user_defined_keys()
        self.assertIsNotNone(user_defined_keys)

    @skipIfNoAuth
    def test_upload_csv(self):
        raise SkipTest("Write tests not yet implemented")  # TODO upload_csv test

    def test_find_by_uuid(self):
        uuid = "eb05c713-9cd9-4cd9-bcaa-71f8e500825d"
        box = boundingboxes.find_by_uuid(uuid)
        self.assertIsNotNone(box)
        self.assertEqual(box.uuid, uuid)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest("Write tests not yet implemented")  # TODO update test

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest("Write tests not yet implemented")  # TODO delete test

    def test_audit_by_uuid(self):
        uuid = "9f31b626-b118-4819-860c-3c1cfc04be3f"
        boxes = boundingboxes.audit_by_uuid(uuid)
        self.assertIsNotNone(boxes)
        self.assertEqual(boxes[0].uuid, uuid)

    def test_audit_by_user_defined_key(self):
        user_defined_key = "285aa889-f771-46c0-6763-c0398712ba1e"
        boxes = boundingboxes.audit_by_user_defined_key(user_defined_key)
        self.assertIsNotNone(boxes)
        self.assertEqual(boxes[0].userDefinedKey, user_defined_key)

    def test_find_searchable_concepts(self):
        searchable_concepts = boundingboxes.find_searchable_concepts()
        self.assertIsNotNone(searchable_concepts)
        self.assertIn("Bathochordaeus", searchable_concepts)

    def test_find_by_observer_uuid(self):
        observer_uuid = "9dba65e1-5974-46df-9276-98c461beba9f"
        boxes = boundingboxes.find_by_observer_uuid(observer_uuid)
        self.assertIsNotNone(boxes)

    def test_find_by_verifier_uuid(self):
        verifier_uuid = "9dba65e1-5974-46df-9276-98c461beba9f"
        boxes = boundingboxes.find_by_verifier_uuid(verifier_uuid)
        self.assertIsNotNone(boxes)

    # def test_audit_by_concepts(self):
    #     concepts = ["Bathochordaeus", "a'a", "Abraliopsis (Boreabraliopsis) felis"]
    #     boxes = boundingboxes.audit_by_concepts(concepts)
    #     self.assertIsNotNone(boxes)

    def test_audit_by_verifier(self):
        verifier = "brian@mbari.org"
        boxes = boundingboxes.audit_by_verifier(verifier)
        self.assertIsNotNone(boxes)

    def test_audit_by_observer(self):
        observer = "brian@mbari.org"
        boxes = boundingboxes.audit_by_observer(observer)
        self.assertIsNotNone(boxes)
