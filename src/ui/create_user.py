from tkinter import ttk, constants, messagebox
from services.service import SERVICE, UsernameExistsError


class CreateUserView:
    """Luokka, joka näyttää näkymän, jossa käyttäjä luodaan
    """
    def __init__(self, root, handle_show_login_view, handle_create_user):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_create_user = handle_create_user
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Vastaa siitä, miten asiat on sijoitettu käyttöliittymään.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        space = " "

        if len(username) == 0 or len(password) == 0:
            messagebox.showerror("empty", "Username and password required")
            return

        if space in username or space in password:
            messagebox.showerror("Invalid characters", "Username or password can't contain empty characters")
            return

        if len(username) < 5:
            messagebox.showerror("username too short",
                                 "Username must be at least 5 characters long")
            return

        if len(password) < 6:
            messagebox.showerror("password too short",
                                 "Password must be at least 6 characters long")
            return

        try:
            SERVICE.create_user(username, password)
            self._handle_create_user()
            messagebox.showinfo("user created", f"User {username} created!")
        except UsernameExistsError:
            messagebox.showerror("username already exists",
                                 f"User {username} already exists")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Create an user",
                          foreground="deep pink", font=("Times 20 bold"))

        label.grid(columnspan=2, sticky=constants.EW, padx=2, pady=2)

        username = ttk.Label(master=self._frame,
                             text="Username: (min. 5 characters)", foreground="deep pink", font=("Times 15"))
        self._username_entry = ttk.Entry(master=self._frame)

        username.grid(row=1, padx=2, pady=2)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.EW), padx=2, pady=2)

        password = ttk.Label(master=self._frame,
                             text="Password: (min. 6 characters)", foreground="deep pink", font=("Times 15"))
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password.grid(padx=2, pady=2)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=2, pady=2)

        button = ttk.Button(master=self._frame,
                            text="Create user", command=self._create_user_handler)

        button2 = ttk.Button(master=self._frame,
                             text="Back", command=self._handle_show_login_view)

        button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button2.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
