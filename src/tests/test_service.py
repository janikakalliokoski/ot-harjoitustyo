import unittest
from entities.user import User
from services.service import (
    InvalidCredentialsError,
    ReviewService,
    UsernameExistsError
)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_users(self):
        return self.users

    def find_by_username(self, username):
        matching = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_list = list(matching)

        return matching_list[0] if len(matching_list) > 0 else None

    def create_user(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = ReviewService(
            FakeUserRepository()
        )

        self.user_janika = User("janika", "abc123")

    def login_user(self, user):
        self.service.create_user(user.username, user.password)

    def test_login_with_valid_credentials(self):
        self.service.create_user(
            self.user_janika.username,
            self.user_janika.password
        )

        user = self.service.login(
            self.user_janika.username,
            self.user_janika.password
        )

        self.assertEqual(user.username, self.user_janika.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.service.login("test", "invalid")
        )

    def test_create_user_successfully(self):
        username = self.user_janika.username
        password = self.user_janika.password

        self.service.create_user(username, password)

        users = self.service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_unsuccessfully(self):
        username = self.user_janika.username

        self.service.create_user(username, "invalid")

        self.assertRaises(
            UsernameExistsError,
            lambda: self.service.create_user(username, "something")
        )

    def test_current_user(self):
        self.login_user(self.user_janika)

        current = self.service.get_current_user()

        self.assertEqual(current.username, self.user_janika.username)
