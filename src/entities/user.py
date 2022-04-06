class User:
    # luokka kuvaa yksittäistä käyttäjää.
    def __init__(self, username, password):
        # konstruktori luo uuden käyttäjän
        self.username = username
        self.password = password
    # attribuutti username kuvaa käyttäjän käyttäjätunnusta
    # attribuutti password kuvaa käyttäjän salasanaa
    # molemmat attribuutit ovat merkkijonoja
