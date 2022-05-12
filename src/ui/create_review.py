from tkinter import ttk, constants, messagebox
from services.service import SERVICE
from entities.review import Review


class CreateReviewview:
    """Luokka, joka näyttää näkymän, jossa arvio ravintolasta luodaan.
    """
    def __init__(self, root, handle_review, user=None):
        self._root = root
        self._handle_review = handle_review
        self._frame = None
        self._name_entry = None
        self._review_entry = None
        self._rating_entry = None
        self._user_entry = None
        self._user = user

        self._initialize()

    def pack(self):
        """Vastaa siitä, miten asiat on sijoitettu käyttöliittymään.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_review_handler(self):
        name = self._name_entry.get()
        review = self._review_entry.get()
        rate = self._rating_entry.get()
        user = self._user_entry.get()

        rates = ["", " ", "1", "2", "3", "4", "5"]

        empty = []
        space = " "

        if space in name or space in review:
            messagebox.showerror("Invalid characters", "Lines can't contain empty characters")
            return

        if len(name) == 0 or len(review) == 0 or len(rate) == 0 or len(user) == 0:
            empty.append(1)

        if user != SERVICE.get_current_user():
            messagebox.showerror("username doesn't match",
                                 "Write the username you logged in with")

        if rate not in rates:
            messagebox.showerror(
                "error in rate", "Rate should be between 1 and 5")
            return

        new = Review(name, review, rate, user)

        if len(empty) != 0:
            messagebox.showerror(
                "empty lines", "Please fill in all the lines")
        elif len(empty) == 0 and user == SERVICE.get_current_user():
            SERVICE.create_review(new)
            messagebox.showinfo("review created", "Review created!")
            self._name_entry.delete(0, "end")
            self._review_entry.delete(0, "end")
            self._rating_entry.delete(0, "end")
            self._user_entry.delete(0, "end")

        return new

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

        user = ttk.Label(master=self._frame, text="Write your username here:",
                         foreground="deep pink", font=("Times 15"))
        self._user_entry = ttk.Entry(master=self._frame)

        user.grid(padx=2, pady=2, sticky=(constants.W))
        self._user_entry.grid(row=4, column=1, sticky=(
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
