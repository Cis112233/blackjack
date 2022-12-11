# Dealer class to represent the computer-controlled dealer and their current cards and total
class Dealer:
    def __init__(self):
        self.cards = []
        self.total = 0

    def hit(self, card):
        self.cards.append(card)
        self.total += card.value

    def stand(self):
        pass

    def bust(self):
        return self.total > 21