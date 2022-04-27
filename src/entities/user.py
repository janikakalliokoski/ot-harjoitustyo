class User:
    """Tämä luokka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: merkkijonoarvo, joka kuvaa käyttäjän käyttäjäyunnusta.
        password: merkkijonoarvo, joka kuvaa käyttäjän tunnukseen liitettyä salasanaa.
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username (str): kuvaa käyttäjän käyttäjätunnusta.
            password (str): kuvaa käyttäjän tunnukseen liitettyä salasanaa.
        """
        self.username = username
        self.password = password
