
from components.games.easy.ecuation1 import ecuation1

def startGame():
    # Here is the room where have to choose random the games
    # Im thinking in every game could be in his own file, and here
    # put them into a list of function and choose 8 randomly

    # easyGames = [ecuation1()]
    # easyGames[0]

    currentPoints = ecuation1()

    print(f"Tu puntaje final durante las 8 partidas es de {currentPoints}\n\n")

    ## here in a cicle choose randomly three easy games, theree mid games an' two hard games

