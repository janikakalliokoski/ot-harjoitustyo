import unittest

from repositories.review_repository import review_repository
from repositories.user_repository import User_repository
from entities.review import Review
from entities.user import User


class TestReviewRepository(unittest.TestCase):
    def setUp(self):
        review_repository.delete_reviews()
        User_repository.delete_users()
        self.user1 = User("janika", "abc123")
        self.user2 = User("sohvi", "sohvi123")
        self.review1 = Review("abc", "nice", "3", self.user1)
        self.review2 = Review("def", "not good", "1", self.user2)

    def test_create_review(self):
        User_repository.create_user(self.user1)

        restaurant = self.review1.restaurant
        review = self.review1.review
        rate = self.review1.rate
        user = self.user1.username

        test_review = Review(restaurant, review, rate, user)

        review_repository.create_review(test_review)

        all_reviews = review_repository.find_reviews()

        self.assertEqual(all_reviews[0].restaurant, restaurant)
        self.assertEqual(all_reviews[0].user, self.user1.username)

    def test_find_reviews(self):
        User_repository.create_user(self.user1)
        User_repository.create_user(self.user2)

        restaurant = self.review1.restaurant
        review = self.review1.review
        rate = self.review1.rate
        user = self.user1.username

        restaurant2 = self.review2.restaurant
        review2 = self.review2.review
        rate2 = self.review2.rate
        user2 = self.user2.username

        test_review = Review(restaurant, review, rate, user)
        test_review2 = Review(restaurant2, review2, rate2, user2)

        review_repository.create_review(test_review)
        review_repository.create_review(test_review2)

        all_reviews = review_repository.find_reviews()

        self.assertEqual(len(all_reviews), 2)
        self.assertEqual(all_reviews[1].rate, "1")

    def test_find_by_restaurant(self):
        User_repository.create_user(self.user1)

        restaurant = self.review1.restaurant
        review = self.review1.review
        rate = self.review1.rate
        user = self.user1.username

        test_review = Review(restaurant, review, rate, user)

        review_repository.create_review(test_review)

        found = review_repository.find_by_restaurant(restaurant)

        self.assertEqual(found.restaurant, restaurant)

    def test_find_by_user(self):
        User_repository.create_user(self.user1)

        restaurant = self.review1.restaurant
        review = self.review1.review
        rate = self.review1.rate
        user = self.user1.username

        test_review = Review(restaurant, review, rate, user)

        review_repository.create_review(test_review)

        found = review_repository.find_reviews_by_user(user)

        self.assertEqual(found[0].user, user)
