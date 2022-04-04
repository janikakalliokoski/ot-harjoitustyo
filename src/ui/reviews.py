from tkinter import ttk, constants

class ReviewsView:
    def __init__(self, root, handle_show_login_view):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading=ttk.Label(master=self._frame, text="Reviews of restaurants visited")
        heading.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        logout_user_button=ttk.Button(master=self._frame, text="Create user", command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        logout_user_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)