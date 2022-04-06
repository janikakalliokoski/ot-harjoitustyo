# luokka yksittäisestä arviosta
# attribuutteina ravintolan nimi, arvostelu,
# User-olio joka kuvaa tehtävän omistajaa ja 

class Review:
    def __init__(self, restaurant, review, user=None):
        self.restaurant = restaurant
        self.review = review
        self.user = user

# konstruktori luo uuden arvostelun
