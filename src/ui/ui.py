from ui.create_review import CreateReviewview
from ui.login import LoginView
from ui.create_user import CreateUserView
from ui.reviews import ReviewsView


class UI:
    """Luokka, joka vastaa näkymien välillä vaihdosta.
    """
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_login(self):
        self._show_login_view()

    def _handle_create_user(self):
        self._show_create_user_view()

    def _handle_reviews(self):
        self._show_reviews_view()

    def _handle_create_review(self):
        self._show_create_review_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._handle_create_user, self._handle_reviews
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root, self._handle_login, self._handle_create_user
        )

        self._current_view.pack()

    def _show_reviews_view(self):
        self._hide_current_view()

        self._current_view = ReviewsView(
            self._root, self._handle_login, self._handle_create_review
        )

        self._current_view.pack()

    def _show_create_review_view(self):
        self._hide_current_view()

        self._current_view = CreateReviewview(
            self._root, self._handle_reviews
        )

        self._current_view.pack()
