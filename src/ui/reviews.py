from tkinter import ttk, constants

from services.service import SERVICE


class ReviewsView:
    def __init__(self, root, handle_login, handle_create):
        self._root = root
        self._handle_login = handle_login
        self._handle_create = handle_create

        self._service = SERVICE
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Reviews of restaurants visited", foreground="deep pink", font=("Times 20 bold"))
        label.grid(columnspan=2, sticky=constants.EW, padx=2, pady=2)

        button2 = ttk.Button(
            master=self._frame, text="Create a review", command=self._handle_create)

        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self.tree = ttk.Treeview(self._frame, columns=(
            "Site", "Username", "Password"
        ))
        self.tree.heading("#0", text="id")
        self.tree.heading("#1", text="Restaurant")
        self.tree.heading("#2", text="Review")
        self.tree.heading("#3", text="Rate")

        self.tree.column("0", width=100)
        self.tree.grid(row=2, columnspan=4, sticky="nsew")

        button = ttk.Button(master=self._frame,
                            text="Log out", command=self._handle_login)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
