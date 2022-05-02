from tkinter import ttk, constants, messagebox
from entities.review import Review
from services.service import SERVICE, ReviewExistsError


class CreateReviewview:
    def __init__(self, root, handle_review):
        self._root = root
        self._handle_review = handle_review
        self._frame = None
        self._name_entry = None
        self._review_entry = None
        self._rating_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_review_handler(self):
        name = self._name_entry.get()
        review = self._review_entry.get()
        rate = self._rating_entry.get()

        rates = ["1", "2", "3", "4", "5"]

        if rate not in rates:
            messagebox.showerror(
                "error in rate", "Rate should be between 1 and 5")
            return
        if len(name) == 0 or len(review) == 0 or len(rate) == 0:
            messagebox.showerror(
                "empty lines", "Name, review and rate required")
            return

        try:
            SERVICE.create_review(name, review, rate)
            self._handle_review()
            messagebox.showinfo("review created!", "Review created!")
        except ReviewExistsError:
            messagebox.showerror(
                "already exists", f"Review of restaurant {review} already exists")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Create a review",
                          foreground="deep pink", font=("Times 20 bold"))

        label.grid(columnspan=2, sticky=constants.EW, padx=2, pady=2)

        name = ttk.Label(master=self._frame,
                         text="Name of the restaurant visited:", foreground="deep pink", font=("Times 15"))
        self._name_entry = ttk.Entry(master=self._frame)

        name.grid(row=1, padx=2, pady=2)
        self._name_entry.grid(row=1, column=1, sticky=(
            constants.EW), padx=2, pady=2)

        review = ttk.Label(master=self._frame, text="Write the review here:",
                           foreground="deep pink", font=("Times 15"))
        self._review_entry = ttk.Entry(master=self._frame)

        review.grid(padx=2, pady=2, sticky=(constants.W))
        self._review_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2)

        rating = ttk.Label(master=self._frame, text="Rate from 1 to 5:",
                           foreground="deep pink", font=("Times 15"))
        self._rating_entry = ttk.Entry(master=self._frame)

        rating.grid(padx=2, pady=2, sticky=(constants.W))
        self._rating_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2)

        button1 = ttk.Button(master=self._frame, text="Ok",
                             command=self._create_review_handler)

        button1.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(master=self._frame, text="Back",
                            command=self._handle_review)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
