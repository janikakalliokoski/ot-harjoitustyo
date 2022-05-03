import unittest

from repositories.user_repository import User_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        User_repository.delete_users()
        self.user1 = User('janika', 'abc123')
        self.user2 = User('isabel', 'isabel123')

    def test_create(self):
        User_repository.create_user(self.user1)
        all_users = User_repository.find_users()
        self.assertEqual(all_users[0].username, self.user1.username)

    def test_find_users(self):
        User_repository.create_user(self.user1)
        User_repository.create_user(self.user2)
        all_users = User_repository.find_users()
        self.assertEqual(all_users[0].username, self.user1.username)
        self.assertEqual(all_users[1].username, self.user2.username)
        self.assertEqual(len(all_users), 2)

    def test_find_by_username(self):
        User_repository.create_user(self.user2)
        user = User_repository.find_by_username(self.user2.username)
        self.assertEqual(user.username, self.user2.username)
