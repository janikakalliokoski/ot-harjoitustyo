from entities.user import User
#from entities.review import Review

from repositories.user_repository import (
    User_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass

# tämä luokka vastaa sovelluslogiikasta


class ReviewService:
    # tämä luokka vastaa sovelluslogiikasta
    def __init__(
            self,
            user_repository=default_user_repository
    ):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_all_users(self):
        return self._user_repository.find_users()

    def logout(self):
        self._user = None

    def create_user(self, username: str, password: str, login=True):
        existing = self._user_repository.find_by_username(username)

        if existing:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user


SERVICE = ReviewService()
