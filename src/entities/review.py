import uuid


class Review:
    """Tämä luokka kuvaa yksittäistä arviota

    Attributes:
        restaurant: merkkijonoarvo, joka kuvaa käydyn ravintolan nimeä.
        review: merkkijonoarvo, joka kuvaa käydyn ravintolan arvostelua.
        user: merkkijonoarvo, joka kuvaa arvostelun luovaa käyttäjää.
        review_id: merkkijonoarvo, joka kuvaa arvostelun id:tä.
    """

    def __init__(self, restaurant, review, rate, user, review_id=None):
        """Luokan konstruktori, joka luo uuden arvion.

        Args:
            restaurant (str): kuvaa käydyn ravintolan nimeä.
            review (str): kuvaa käydyn ravintolan arvostelua.
            starts (str): kuvaa kuinka monta tähteä (1-5) käyttäjä antaa ravintolalle.
            user (str): kuvaa arvion kirjoittajaa.
                         kuvaa arvostelun omistavaa käyttäjää.
            review_id (str): vapaaehtoinen, oletusarvoltaan generoitu uuid.
                             kuvaa tehtävän id:tä
        """

        self.restaurant = restaurant
        self.review = review
        self.rate = rate
        self.user = user
        self.id = review_id or str(uuid.uuid4())
