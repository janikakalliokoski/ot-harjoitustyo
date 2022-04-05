import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user1 = User('janika', 'abc123')
        self.ur = UserRepository("test_users.db")
        self.ur.create_table()


    def test_create(self):
        self.ur.create_user(self.user1)
        all = self.ur.find_users()
        self.assertEqual(all, [(1, 'janika', 'abc123')])