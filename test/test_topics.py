from unittest import SkipTest, TestCase

from fathomnet.api import topics

from . import skipIfNoAuth


class TestTopicsAPI(TestCase):
    @skipIfNoAuth
    def test_create(self):
        raise SkipTest("Write tests not yet implemented")

    def test_find_by_uuid(self):
        uuid = "411fa644-4f24-49c3-bdc1-b40f91aecaab"
        topic = topics.find_by_uuid(uuid)
        self.assertIsNotNone(topic)

    @skipIfNoAuth
    def test_update(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_delete(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_find(self):
        res_topics = topics.find()
        self.assertIsNotNone(res_topics)

    @skipIfNoAuth
    def test_find_by_email(self):
        raise SkipTest("Not implemented")
