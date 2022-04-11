from tkinter import ttk, constants, StringVar
from services.service import SERVICE, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_show_login_view, handle_create_user):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_create_user = handle_create_user
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

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return

        if len(username) < 5:
            self._show_error("Username must be at least 5 characters long")
            return

        if len(password) < 6:
            self._show_error("Password must be at least 6 characters long")
            return

        try:
            SERVICE.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

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

        heading = ttk.Label(master=self._frame, text="Create user")

        heading.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username = ttk.Label(master=self._frame,
                             text="Username (min. 5 characters)")
        self._username_entry = ttk.Entry(master=self._frame)

        username.grid(padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password = ttk.Label(master=self._frame,
                             text="Password (min. 6 characters)")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password.grid(padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button = ttk.Button(master=self._frame,
                            text="Create user", command=self._create_user_handler)

        button2 = ttk.Button(master=self._frame,
                            text="Back", command=self._handle_show_login_view)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._hide_error()
        
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
