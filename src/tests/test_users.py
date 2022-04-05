import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.ur = UserRepository("tests.db")
        self.ur.delete_table()
        self.ur.create_table()
        self.user1 = User('janika', 'abc123')

    def test_create(self):
        self.ur.create_user(self.user1)
        all = self.ur.find_users()
        self.assertEqual(all, [(1, 'janika', 'abc123')])

# yritettiin pajassa ohjaajan kanssa tunti saada testiä toimimaan mutta taulun users1 nimeä pitää muuttaa joka kerta kun testi suoritetaan jotta se menee läpi
# tässä kansiossa kuva testistä joka on mennyt läpi