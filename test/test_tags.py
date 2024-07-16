from unittest import SkipTest, TestCase

from fathomnet.api import tags

from . import skipIfNoAuth


class TestTagsAPI(TestCase):
    @skipIfNoAuth
    def test_create_with_dto(self):
        raise SkipTest("Write tests not yet implemented")  # TODO create_with_dto test

    def test_find_by_uuid(self):
        uuid = "4c7f468c-ab41-4003-a048-d194a5f4ff4a"
        tag = tags.find_by_uuid(uuid)
        self.assertIsNotNone(tag)
        self.assertEqual(tag.uuid, uuid)

    def test_find_by_image_uuid_and_key(self):
        image_uuid = "70df75b3-02ad-4a33-a5c6-6ed90313f752"
        key = "source"
        tag_list = tags.find_by_image_uuid_and_key(image_uuid, key)
        self.assertIsNotNone(tag_list)
        tag = tag_list[0]
        self.assertEqual(tag.key, key)
        self.assertEqual(tag.value, "MBARI/VARS")
        self.assertEqual(tag.imageUuid, image_uuid)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest("Write tests not yet implemented")  # TODO update test

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest("Write tests not yet implemented")  # TODO delete test
