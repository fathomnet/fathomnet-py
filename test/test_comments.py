from unittest import SkipTest, TestCase

from fathomnet.api import comments

from . import skipIfNoAuth


class TestCommentsAPI(TestCase):
    @skipIfNoAuth
    def test_create(self):
        raise SkipTest("Write tests not yet implemented")

    def test_find_by_uuid(self):
        uuid = "c3e98572-89ab-40ac-8ec1-2cc388b129dc"
        comment = comments.find_by_uuid(uuid)
        self.assertIsNotNone(comment)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def find_by_bounding_box_uuid(self):
        bounding_box_uuid = "c4822967-13b7-435d-9cba-5a7f52f7457f"
        res_comments = comments.find_by_bounding_box_uuid(bounding_box_uuid)
        self.assertIsNotNone(res_comments)

    @skipIfNoAuth
    def test_find_by_email(self):
        email = "erm.butler@gmail.com"
        res_comments = comments.find_by_email(email)
        self.assertIsNotNone(res_comments)

    @skipIfNoAuth
    def test_flag(self):
        raise SkipTest("Write tests not yet implemented")
