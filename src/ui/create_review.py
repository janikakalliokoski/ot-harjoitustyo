from tkinter import ttk, constants


class CreateReviewview:
    def __init__(self, root, handle_back):
        self._root = root
        self._handle_back = handle_back
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading = ttk.Label(master=self._frame, text="Create user")

        heading.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        name = ttk.Label(master=self._frame,
                         text="Name of the restaurant visited")
        name_entry = ttk.Entry(master=self._frame)

        name.grid(padx=5, pady=5)
        name_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        review = ttk.Label(master=self._frame, text="Write here the review")
        review_entry = ttk.Entry(master=self._frame)

        review.grid(padx=5, pady=5)
        review_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(master=self._frame, text="Back",
                            command=self._handle_back)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
