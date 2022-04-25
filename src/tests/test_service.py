import unittest
from entities.user import User
from services.service import (
    SERVICE,
    InvalidCredentialsError,
    UsernameExistsError
)

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_list = list(matching)

        return matching_list[0] if len(matching_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []

