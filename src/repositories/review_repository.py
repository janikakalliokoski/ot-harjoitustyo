from entities.review import Review
from database_connection import get_database_connection


def get_review_by_row(row):
    """hakee arvostelun nimellä

    Args:
        row
    """

    return Review(row["restaurant"], row["review"], row["rate"], row["user"]) if row else None


class ReviewRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_review(self, review):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert or ignore into reviews (restaurant, review, rate, user) values (?,?,?,?)",
                       (review.restaurant, review.review, review.rate, review.user))

        self._connection.commit()
        return review

    def find_reviews_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews where (user) = (?,?)", (user.username))
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def find_by_restaurant(self, restaurant):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews where restaurant = ?",
            (restaurant,)
        )
        restaurant = cursor.fetchone()
        return get_review_by_row(restaurant)

    def find_by_restaurant_and_user(self, restaurant, user):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews, users where restaurant=? and user=?", [restaurant, user])
        review = cursor.fethcone()
        return get_review_by_row(review)

    def find_reviews(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from reviews")
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def delete_reviews(self):
        cursor = self._connection.cursor()

        cursor.execute("delete from reviews")

        self._connection.commit()


review_repository = ReviewRepository(get_database_connection())
