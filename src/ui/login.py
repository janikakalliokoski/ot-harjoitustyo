from tkinter import ttk, constants, StringVar
from services.service import service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_create_user, handle_login):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        heading_label = ttk.Label(master=self._frame, text="Login")

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username.grid(padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password.grid(padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(master=self._frame, text="Login",
                            command=self._login_handler)
        button2 = ttk.Button(
            master=self._frame, text="Create user", command=self._handle_create_user)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._hide_error()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
