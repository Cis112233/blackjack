# Player class to represent the player and their current cards and total
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total = 0

    def hit(self, card):
        self.cards.append(card)
        self.total += card.value

    def stand(self):
        pass

    def bust(self):
        return self.total > 21