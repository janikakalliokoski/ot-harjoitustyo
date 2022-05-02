class User:
    """Tämä luokka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: merkkijonoarvo, joka kuvaa käyttäjän käyttäjäyunnusta.
        password: merkkijonoarvo, joka kuvaa käyttäjän tunnukseen liitettyä salasanaa.
    """

    def __init__(self, username, password, user_id=None):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username (str): kuvaa käyttäjän käyttäjätunnusta.
            password (str): kuvaa käyttäjän tunnukseen liitettyä salasanaa.
        """
        self.username = username
        self.password = password
        self.user_id = user_id

    def set_user_id(self, user_id):
        self.user_id = user_id
