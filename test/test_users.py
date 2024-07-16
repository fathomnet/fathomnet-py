from unittest import SkipTest, TestCase

from fathomnet.api import users
from fathomnet.dto import Pageable

from . import skipIfNoAuth


class TestUsersAPI(TestCase):
    @skipIfNoAuth
    def test_create_with_dto(self):
        raise SkipTest("Write tests not yet implemented")  # TODO create_with_dto test

    @skipIfNoAuth
    def test_find_all(self):
        pageable = Pageable(size=5)
        res_users = users.find_all(pageable)
        self.assertIsNotNone(res_users)

    @skipIfNoAuth
    def test_find_all_admin(self):
        raise SkipTest("Not implemented")

    @skipIfNoAuth
    def test_update_user_data(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_update_user_data_admin(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_get_api_key(self):
        api_key = users.get_api_key()
        self.assertIsNotNone(api_key)

    @skipIfNoAuth
    def test_create_new_api_key(self):
        raise SkipTest("Write tests not yet implemented")

    @skipIfNoAuth
    def test_delete_api_key(self):
        raise SkipTest("Write tests not yet implemented")

    def test_count_all(self):
        count = users.count_all()
        self.assertIsNotNone(count)
        self.assertEqual(count.objectType, "FathomnetIdentityEntity")
        self.assertGreater(count.count, 0)

    @skipIfNoAuth
    def test_disable_by_uuid(self):
        raise SkipTest("Write tests not yet implemented")

    def test_find_expertise(self):
        expertise = users.find_expertise()
        self.assertIsNotNone(expertise)

    def test_find_contributors_names(self):
        contributors = users.find_contributors_names()
        self.assertIsNotNone(contributors)

    def test_find_roles(self):
        roles = users.find_roles()
        self.assertIsNotNone(roles)

    @skipIfNoAuth
    def test_find_by_authentication(self):
        user = users.find_by_authentication()
        self.assertIsNotNone(user)

    def test_find_by_firebase_uid(self):
        raise SkipTest("Not yet implemented")

    @skipIfNoAuth
    def test_verify(self):
        auth = users.verify()
        self.assertIsNotNone(auth)

    def test_find_by_display_name(self):
        res_users = users.find_by_display_name("Brian")
        self.assertIsNotNone(res_users)

    @skipIfNoAuth
    def test_find_by_organization(self):
        res_users = users.find_by_organization("mbari")
        self.assertIsNotNone(res_users)

    def test_find_by_uuid(self):
        res_user = users.find_by_uuid("9dba65e1-5974-46df-9276-98c461beba9f")
        self.assertIsNotNone(res_user)

    def test_find_badges_by_uuid(self):
        res_badges = users.find_badges_by_uuid("9dba65e1-5974-46df-9276-98c461beba9f")
        self.assertIsNotNone(res_badges)
