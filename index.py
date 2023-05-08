
## external imports 

## own imports
from components.register.register import registerUser
from components.score.score import watchScore
from components.games.room import startGame


try:
    
    option = "",
    isPlaying = True

    print("Bienvenido al Juego de acertijos matematicos, que deseas hacer?")

    while(isPlaying):

        print("1. Registrar jugador")
        print("2. Verificar puntuaciones")
        print("3. Jugar")
        print("4. Salir")

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