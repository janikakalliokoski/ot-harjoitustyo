from entities.review import Review
from database_connection import get_database_connection


def get_review_by_row(row):
    """hakee arvostelun nimellä

    Args:
        row
    """

    return Review(row["restaurant"], row["review"], row["rate"]) if row else None


class ReviewRepository:
    def __init__(self, connection):
        self._connection = connection

    def change_type(self, review):
        if not review:
            return None

        res = Review(review[0], review[1], review[2])
        res.set_user(review[3])

    def create_review(self, review):
        cursor = self._connection.cursor()

        cursor.execute("insert into reviews (restaurant, review, rate, user) values (?,?,?,?)",
                       (review.restaurant, review.review, review.rate, review.user))

        self._connection.commit()
        return review

    def find_reviews_by_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("select * from reviews where user = ?", (user.user_id,))
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def find_by_name(self, restaurant):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from reviews where restaurant = ?",
            (restaurant,)
        )
        user = cursor.fetchone()
        return get_review_by_row(user)

    def find_reviews(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from reviews")
        reviews = cursor.fetchall()
        return list(map(get_review_by_row, reviews))

    def delete_reviews(self):
        cursor = self._connection.cursor()

        cursor.execute("delete from items")

        self._connection.commit()


review_repository = ReviewRepository(get_database_connection())
