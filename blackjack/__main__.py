
from classes.startround import start_round

def __main__():
    play = True
    player_name = input("Enter your name: ")
    while play:
        start_round(player_name)

        answer = input("Do you want to play again (y/n): ")
        
        if(answer != "y"):
            play = False

__main__()