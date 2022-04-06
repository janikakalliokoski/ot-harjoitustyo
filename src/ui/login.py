from tkinter import ttk, constants


class LoginView:
    def __init__(self, root, handle_create_user, handle_login):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_login = handle_login
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Login")

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(master=self._frame, text="Login",
                            command=self._handle_login)
        button2 = ttk.Button(
            master=self._frame, text="Create user", command=self._handle_create_user)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
