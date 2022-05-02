from entities.user import User

from repositories.user_repository import (
    User_repository as default_user_repository
)

from repositories.review_repository import (
    review_repository as default_review_repository
)


class InvalidCredentialsError(Exception):
    """luokka, joka tuottaa virheen jos käyttäjänimi ja/tai salasana on virheellinen.

    Args:
        Exception
    """
    pass


class UsernameExistsError(Exception):
    """luokka, joka tuottaa virheen jos käyttäjätunnus on valmiiksi jo olemassa

    Args:
        Exception
    """
    pass


class ReviewService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(
            self,

            user_repository=default_user_repository,
            review_repository=default_review_repository
    ):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            user_repository (UserRepository):
                        Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                        Olio, jolla on UserRepository-luokkaa vastaavat metodit.
            review_repository (ReviewRepository):
                        Vapaaehtoinen, oletusarvoltaan ReviewRepository-olio.
                        Olio, jolla on ReviewRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        self._user_repository = user_repository
        self._review_repository = review_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username (str): kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password (str): Kuvaa kirjautuvan käyttäjän salasanaa.

        Raises:
            InvalidCredentialsError:
                        Virhe, joka tapahtuu, jos käyttäjätunnus ja salasana eivät täsmää.

        Returns:
            User: kirjautunut käyttäjä jos se löytyy tietokannasta.
        """

        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            User: kirjautunut käyttäjä.
        """

        return self._user

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät jotka löytyvät tietokannasta.

        Returns:
            list: lista kaikista käyttäjistä User-olioina
        """

        return self._user_repository.find_users()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """

        self._user = None

    def create_user(self, username: str, password: str, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa käyttäjän sisään.

        Args:
            username (str): kuvaa käyttäjän käyttäjätunnusta.
            password (str): kuvaa käyttäjän käyttäjätunnuksen salasanaa.
            login (bool): vapaaehtoinen, oletusarvoltaan True.
                          kertoo, kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExistsError: virhe, joka tapahtuu jos käyttäjätunnus löytyy jo tietokannasta.

        Returns:
            User: luotu käyttäjä.
        """

        existing = self._user_repository.find_by_username(username)

        if existing:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user

    def find_reviews_by_user(self, user):
        reviews = self._review_repository.find_reviews_by_user(user)

        return reviews

    def create_review(self, review):
        new = self._review_repository.create_review(review)

        return new


SERVICE = ReviewService()
