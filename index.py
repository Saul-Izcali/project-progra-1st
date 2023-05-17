
## external imports 

## own imports
from components.register.register import registerUser
from components.score.score import watchScore
from components.games.room import startGame
from utils.colors.colors import bcolors

try:
    
    option = "", 
    isPlaying = True

    print(bcolors.OKBLUE + "\nBienvenido al Juego de acertijos matematicos, que deseas hacer?\n" + bcolors.ENDC)

    while(isPlaying):

        print(bcolors.OKBLUE + "1.- " + bcolors.ENDC + "Registrar jugador")
        print(bcolors.OKBLUE + "2.- " + bcolors.ENDC + "Verificar puntuaciones")
        print(bcolors.OKBLUE + "3.- " + bcolors.ENDC + "Jugar")
        print(bcolors.OKBLUE + "4.- " + bcolors.ENDC + "Salir")

        option = input("\n")

        if (option == "1"):
            registerUser()

        elif (option == "2"):
            watchScore()

        elif (option == "3"):
            startGame()

        elif (option == "4"):
            isPlaying = False
            print("Hasta luego.")

        else:
            print("Ingresa una opción válida\n")
            

except:
    print("Error")