from entities.review import Review
from database_connection import get_database_connection


def get_review_by_row(row):
    """hakee arvostelun.

    Args:
        row
    """

    return Review(row["restaurant"], row["review"], row["rate"], row["user"]) if row else None


class ReviewRepository:
    """Tietokantaluokka arvosteluista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection (Connection): Connection-olio joka kuvaa tietokantayhteyttä.
        """
        self._connection = connection

    def create_review(self, review):
        """Lisää arvostelun tietokantaan.

        Args:
            review (Review): Review-olio, joka lisätään tietokantaan.

        Returns:
            Review: palauttaa lisätyn Review-olion.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert or ignore into reviews (restaurant, review, rate, user) values (?,?,?,?)",
            (review.restaurant, review.review, review.rate, review.user))

        self._connection.commit()
        return review

    def find_reviews_by_user(self, user):
        """Löytää tietyn käyttäjän tekemät arviot.

        Args:
            user (User): User-olio, käyttäjä, jonka tekemät arvostelut haetaan.

        Returns:
            list: Palauttaa halutun käyttäjän arviot listana.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews where user=?", (user,))
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def find_by_restaurant(self, restaurant):
        """Hakee tietystä ravintolasta tehdyn arvostelun tietokannasta.

        Args:
            restaurant (str): Review-olion attribuutti restaurant.

        Returns:
            Review: Palauttaa arvostelun ravintolasta Review-oliona.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews where restaurant = ?",
            (restaurant,)
        )
        restaurant = cursor.fetchone()
        return get_review_by_row(restaurant)

    def find_reviews(self):
        """Hakee tietokannasta kaikki arvostelut.

        Returns:
            list: Palauttaa listan Review-olioita.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from reviews")
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def delete_reviews(self):
        """Poistaa kaikki tehdyt arvostelut tietokannasta.
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from reviews")

        self._connection.commit()


review_repository = ReviewRepository(get_database_connection())
