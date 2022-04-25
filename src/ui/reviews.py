from tkinter import ttk, constants


class ReviewsView:
    def __init__(self, root, handle_login, handle_create):
        self._root = root
        self._handle_login = handle_login
        self._handle_create = handle_create
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading = ttk.Label(master=self._frame,
                            text="Reviews of restaurants visited")
        heading.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        button = ttk.Button(master=self._frame,
                            text="Log out", command=self._handle_login)
        button2 = ttk.Button(master=self._frame, text="Create a review", command=self._handle_create)

        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
