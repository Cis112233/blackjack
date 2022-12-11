from classes.card import Card
import random
# Deck class to represent the deck of cards and provide methods for shuffling and dealing
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()