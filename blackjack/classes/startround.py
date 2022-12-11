from classes.card import Card 
from classes.deck import Deck 
from classes.dealer import Dealer 
from classes.players import Player
import random

# Function to start a new round of blackjack
def start_round(player_name):
    # Ask the player for their name and create a Player object
    
    player = Player(player_name)

    # Create a Dealer object
    dealer = Dealer()

    # Shuffle the deck and deal two cards to the player and dealer
    deck = Deck()
    deck.shuffle()
    player.hit(deck.deal())
    player.hit(deck.deal())
    dealer.hit(deck.deal())
    dealer.hit(deck.deal())

    # Player turn: hit or stand
    print(f"Your cards are: {player.cards[0].give_value()} and {player.cards[1].give_value()}")
    print(f"You see the dealer has: {dealer.cards[0].give_value()} visable and one card hidden")
    while True:
        action = input("Hit or stand? [H/S] ")
        if action.lower() == "h":
            player.hit(deck.deal())
            
            print("Your cards are: ")
            for carder in player.cards:
                print(carder.give_value())
            if player.bust():
                print()
                print(f"{player.name} busts!\n Dealer wins with a hand of:")

                for carder in dealer.cards:
                    print(carder.give_value())
                print()
                break
        elif action.lower() == "s":
            break
        else:
            print("Invalid action. Please try again.")

    # Dealer turn: hit or stand
    if not player.bust():
        while dealer.total < 17:
            dealer.hit(deck.deal())
        if dealer.bust():
            print(f"Dealer busts! {player.name} wins with: ")
            for carder in player.cards:
                    print(carder.give_value())
        elif dealer.total > player.total:
            print(f"Dealer wins with a total of {dealer.total}.")
            
        elif dealer.total == player.total:
            print(f"It's a tie!")
        elif dealer.total < player.total:
            print(f"{player.name} wins with a total of {player.total}")
    
