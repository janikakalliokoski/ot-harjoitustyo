import sqlite3

from entities.user import User

class UserRepository:
    def __init__(self, name):
        self.db = sqlite3.connect(name)
        self.db.isolation_level = None
        self.name = name

    def create_table(self):
        self.db.execute("begin")
        self.db.execute(
            "create table users1 (id integer primary key, name text, password text)")
        self.db.execute("commit")

    def create_user(self, user: User):
        self.db.execute("begin")
        self.db.execute("insert into users1 (name, password) values (?,?)",
                        [user.username, user.password])
        self.db.execute("commit")
        return user

    def find_users(self):
        self.db.execute("begin")
        all_users = self.db.execute("select * from users1").fetchall()
        self.db.execute("commit")
        return all_users

    def find_by_username(self, username):
        self.db.execute("begin")
        found_user = self.db.execute("select * from users1 where username = ?", (username,)).fetchone()
        self.db.execute("commit")
        return found_user

    def delete_table(self):
        self.db.execute("begin")
        self.db.execute("drop table users1")
        self.db.execute("commit")


if __name__ == "__main__":
    U = UserRepository()
    U.create_table()
