# Card class to represent a single playing card with suit and value attributes
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def give_value(self):
        return f"{self.value} of {self.suit}"