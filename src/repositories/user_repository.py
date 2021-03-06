from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    """hakee käyttäjän.

    Args:
        row

    Returns:
        User-olio
    """
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Tietokantaluokka käyttäjistä.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (Connection): Connection-olio joka kuvaa tietokantayhteyttä.
        """

        self._connection = connection

    def create_user(self, user):
        """Lisää käyttäjän tietokantaan.

        Args:
            user (User): User-olio, joka lisätään tietokantaan.

        Returns:
            User: palauttaa lisätyn User-olion.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?,?)",
            (user.username, user.password)
        )

        self._connection.commit()
        return user

    def find_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            list: palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()
        return list(map(get_user_by_row, users))

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username (str): käyttäjätunnus, jonka käyttäjä palautetaan.

        Returns:
                User:
                palauttaa User-olion, jos käyttäjätunnuksen omistana käyttäjä löytyy tietokannasta.
                muuten palauttaa None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        user = cursor.fetchone()
        return get_user_by_row(user)

    def delete_users(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


User_repository = UserRepository(get_database_connection())
