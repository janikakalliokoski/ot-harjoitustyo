from tkinter import Tk, ttk, constants

class LoginView:
    def __init__(self,root):
        self._root = root

    def start(self):
        heading=ttk.Label(master=self._root, text="Login")

        username=ttk.Label(master=self._root, text="Username")
        username_entry=ttk.Entry(master=self._root)

        password=ttk.Label(master=self._root, text="Password")
        password_entry=ttk.Entry(master=self._root, show="*")

        button=ttk.Button(master=self._root, text="Login")
        button2=ttk.Button(master=self._root, text="Create user")

        heading.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button2.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

window = Tk()
window.configure(bg='hot pink')
window.title("Login")

ui = LoginView(window)
ui.start()

window.mainloop()