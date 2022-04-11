import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_users()
        self.user1 = User('janika', 'abc123')
        self.user2 = User('isabel', 'isabel123')

    def test_create(self):
        user_repository.create_user(self.user1)
        all = user_repository.find_users()
        self.assertEqual(all[0].username, self.user1.username)

    def test_find_users(self):
        user_repository.create_user(self.user1)
        user_repository.create_user(self.user2)
        all = user_repository.find_users()
        self.assertEqual(all[0].username, self.user1.username)
        self.assertEqual(all[1].username, self.user2.username)

    def test_find_by_username(self):
        user_repository.create_user(self.user2)
        user = user_repository.find_by_username(self.user2.username)
        self.assertEqual(user.username, self.user2.username)
