import random
import os
import time
from IPython.display import clear_output, Image, display
# from utils.seeders.players import players

# from google.colab import drive
# drive.mount('/content/drive')

# Diccionario para almacenar las puntuaciones de los jugadores
## eso es un arreglo de pruebas
registro_jugadores = [
    {
        "nombre": "saul",
        "puntaje_partidas": [
            10, 30, 0, 100
        ],
        "puntaje_total": 140,
    },
    {
        "nombre": "izcali",
        "puntaje_partidas": [
            45
        ],
        "puntaje_total": 45,
    },
    {
        "nombre": "pepe",
        "puntaje_partidas": [
            15, 90
        ],
        "puntaje_total": 105,
    },
    {
        "nombre": "juan",
        "puntaje_partidas": [
            120, 5, 75
        ],
        "puntaje_total": 200,
    },
]

# cuando no sea una prueba cambiarlo por un array vacio
# registro_jugadores = []
puntuacion = []
nombre = ''

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Emojis:
    CORRECT = ' \U00002705 '
    ERROR = ' \U0000274C '


def mostrar_menu_principal(): 
    print(Colors.OKBLUE + "\n---- MENÚ PRINCIPAL ----" + Colors.ENDC)
    print("1. Registrar jugador")
    print("2. Verificar puntuaciones")
    print("3. Jugar")
    print("4. Salir")


def loading():
    os.system('cls')
    clear_output()
    print("\n\nCargando ▓▒▒▒▒▒▒▒▒▒ 10%")
    time.sleep(0.3)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▒▒▒▒▒▒▒▒ 20%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▒▒▒▒▒▒▒ 30%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▒▒▒▒▒▒ 40%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▒▒▒▒▒ 50%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▓▒▒▒▒ 60%")
    time.sleep(0.3)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▓▓▒▒▒ 70%")
    time.sleep(0.2)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▓▓▓▒▒ 80%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▓▓▓▓▒ 90%")
    time.sleep(0.1)
    clear_output()
    os.system('cls')
    print("\n\nCargando ▓▓▓▓▓▓▓▓▓▓ 100%")
    time.sleep(0.5)
    clear_output()
    os.system('cls')


def buscar_jugador(nombre_a_buscar):
    ## cada que va a buscar si un jugador existe ordena la lista de jugadores con base a su puntaje total
    ## del puntaje mas alto al mas bajo
    ## entonces el indice que retorna es directamente que su posicion
    ## (claro, recuerda que una lista inicia en la posicion 0)
    ## esto (la siguiente linea) idealmente solo deberia estar cada que termina una partida, lo dejo aqui de mientras para las pruebas
    registro_jugadores.sort(key=lambda x: x['puntaje_total'], reverse=True)

    for (index, jugador) in enumerate(registro_jugadores):
        if jugador['nombre'] == nombre_a_buscar:
            return { 'existe': True, 'posicion': index }
        
    ## en caso de no encontrar el jugador buscado retorna un objeto con una bandera y la posicion como ninguna,
    ## porque no existe
    return { 'existe': False, 'posicion': None }
    


def registrar_jugador():
    nombre = input("Ingrese el nombre del jugador: ")
    nombre = nombre.casefold()

    existe_jugador = buscar_jugador(nombre)

    ## cuando se comprueba que el jugador no ha sido registrado
    ## ingresa todos los datos del jugador a la final d ea lista de 'registro de jugadores
    if existe_jugador['existe'] == False:
        dato_jugador = {
            "nombre": nombre,
            "puntaje_partidas": [],
            "puntaje_total": 0,
        }
        registro_jugadores.extend([dato_jugador])
        clear_output()
        print(f"El Jugador {nombre} Ha Sido Registrado Exitosamente!\n\nVolviendo Al Menu Principal")
        time.sleep(5)
        clear_output()

    else:
        clear_output()
        print("El jugador ya está registrado.\nIngrese un nombre distinto.")
        time.sleep(5)
        clear_output()
        registrar_jugador()

    clear_output()
    os.system('cls')

def no_registrado():
    ELI = input("Nota: El Jugador Tiene Que Estar Registrado Previamente\n\nElija Un Numero Para Continuar:\n\n1) Intentar Otro Nombre\n2) Regresar al menu\n")

    clear_output()
    os.system('cls')
    # Verificar si el jugador existe en las puntuaciones
    if ELI == "1":
        
        verificar_puntuaciones()

    elif ELI == "2":
        main()
        return
    else: 
        print("Opcion No Valida, Vuelva a Intentarlo")
        time.sleep(5)
        no_registrado()
    clear_output()
    os.system('cls')
    time.sleep(3)    
    clear_output()
    os.system('cls')


def verificar_puntuaciones():
    nombre = input("Ingrese el nombre del jugador: ")
    nombre = nombre.casefold()

    loading()

    existe_jugador = buscar_jugador(nombre)

    # Verificar si el jugador existe en las puntuaciones
    if existe_jugador['existe'] == False:
        print("ERROR: El jugador NO está registrado!\n\n")
        time.sleep(3)
        clear_output()
        os.system('cls')
        no_registrado()
        return
    
    ## itera todos los puntajes de las partidas del jugador buscado
    print(f"Hola {nombre} tus puntuaciones son las siguientes: ")
    for (index, puntaje) in enumerate(registro_jugadores[existe_jugador['posicion']]['puntaje_partidas']):
        print(f"Partida {index + 1} -> {puntaje}")

    print(f"\nTu total de puntos es de {registro_jugadores[existe_jugador['posicion']]['puntaje_total']}")
    print(f"\nActualmente estas en la posición {existe_jugador['posicion'] + 1}")

    ## itera todo 
    print(f"\n EL RANKING ACTUAL ES:")
    for (index, jugador) in enumerate(registro_jugadores):
        print(f"{index + 1} .- {jugador['nombre']} con {jugador['puntaje_total']} puntos")

    time.sleep(10)    


# Función para generar un acertijo aleatorio
def AcertijoFacil():
    # Aquí puedes definir tus propios acertijos matemáticos
    AcertijosFaciles = [
        {"pregunta": "Tengo 3 manzanas y como 2. ¿Cuántas manzanas me quedan?", "respuesta": "1"},
        {"pregunta": "Calcula el resultado de: 15 + 7", "respuesta": "22"},
        {"pregunta": "Calcula el doble de 6", "respuesta": "12"},
        {"pregunta": "Calcula el producto de 5 por 4", "respuesta": "20"},
        {"pregunta": "Calcula el resultado de: 12 ÷ 3", "respuesta": "4"},
        {"pregunta": "Realiza la siguiente operación: 3 + 2 × 4", "respuesta": "11"},
        {"pregunta": "Calcula el triple de 3", "respuesta": "9"},
        {"pregunta": "Calcula el resultado de: 7 - 3 + 2", "respuesta": "6"},
        {"pregunta": "Realiza la siguiente operación: 5 × (2 + 3)", "respuesta": "25"},
        {"pregunta": "Calcula el resultado de: 18 ÷ 6", "respuesta": "3"},
    ]
    return random.choices(AcertijosFaciles, k=3)


def AcertijoMedio():
    AcertijosMedios = [
        {"pregunta": "En una clase de matemáticas, el 60% de los estudiantes son mujeres y el resto son hombres. Si hay 120 estudiantes en total, ¿cuántos estudiantes hombres hay en la clase?", "respuesta": "48"},
        {"pregunta": "Un peaton recorre 34 km en dirección hacia el sur. Después, camina otros 19 km en dirección este. Por último, viaja 6 km más hacia el norte, ¿cuántos kilómetros ha recorrido?","respuesta":"59"},
        {"pregunta": "Entre 3 personas se encuentran dos padres y x hijos. ¿Cuantos hijos hay?","respuesta":"2"},
        {"pregunta": "Una pelota y un bate tienen un precio conjunto de 110 pesos. El bate tiene un valor de 100 pesos superior al de la pelota. ¿Qué precio tiene la pelota?","respuesta":"5"},
        {"pregunta": "¿Si un tren va a 320 km/h cuantos kilometros viajara en 120 minutos?", "respuesta":"640"},
        {"pregunta":"¿Cuántos 9 hay entre el 1 y el 100?", "respuesta":"20"},
        {"pregunta":"Número de 3 dígitos. El dígito que está en el medio es 4 veces mayor que el tercer y último dígito. Además, el primero es 3 unidades más pequeño que el segundo. ¿Qué número es?","respuesta":"141"},
        {"pregunta": "¿Cuántas ocasiones se puede restar el 1 al número 1.111 antes de ser negativo?", "respuesta": "1"},
        {"pregunta": "Un granjero tiene 40 cerdos, 10 conejos y 20 caballos. Si llamas 'caballos' a los 'cerdos', ¿cuántos caballos tendrá ahora?", "respuesta": "60"},
        {"pregunta": "Un padre tiene la edad de su hija multiplicada por 4. En 20 años, este padre tendrá el doble de años que su hija. ¿Qué edad tienen ahora el padre?", "respuesta": "40"},
    ]   
    return random.choices(AcertijosMedios, k=3)


def AcertijoDificil():
    AcertijosDificiles = [
        {"pregunta": "¿En qué momento será correcta la operación 11+3=2?", "respuesta": "14"},
        {"pregunta": "x * ((3 ^ 3) + 6) + 4 - 200 = 224\n¿Cuanto Da X?", "respuesta": "28"},
        {"pregunta": "si x vale 13 y z vale 3, cual es el resultado de x^y", "respuesta": "169"},
        {"pregunta": "La suma de las edades de un padre y su hijo es 66. El padre tiene el doble de edad que tiene el hijo ahora. ¿Cuántos años tiene el Hijo?", "respuesta": "22"},
        {"pregunta": "Si tienes un número de cuatro dígitos donde el primer dígito es la mitad del último dígito,\nel segundo digito es la mitad del primero y el tercer digito es la mitad del segundo, ¿cuál es ese número?", "respuesta": "4218"},
        {"pregunta": "Tengo tres números enteros consecutivos. La suma de los tres números es 72. ¿Cuáles es el primer número de los tres?", "respuesta": "23"},
        {"pregunta": "¿Cual es la raiz cubica de x, si x + 5 = 13 ?", "respuesta": "2"},
        {"pregunta": "Si divido un número por 3 y luego le resto 7, el resultado es 5. ¿Cuál es el número?", "respuesta": "36"},
        {"pregunta": "Si divido un número entre 3, le sumo 12 y luego le resto 6, obtengo 21. ¿Cuál es el número?", "respuesta": "45"},
        {"pregunta": "Un tanque de agua tiene una capacidad de 500 litros. El tanque se llena a una velocidad constante de 10 litros por minuto,\nmientras que al mismo tiempo se vacía a una velocidad constante de 5 litros por minuto. Si el tanque comienza vacío, ¿cuántos minutos tomará llenar completamente el tanque?", "respuesta": "100"},
    ]

    return random.choices(AcertijosDificiles, k=2)



# Función para jugar
def jugar():
    nombre = input("Ingrese el nombre del jugador: ")
    nombre = nombre.casefold()

    time.sleep(2)
    clear_output()
    os.system('cls')
    existe_jugador = buscar_jugador(nombre)
    if existe_jugador['existe'] == False:
        print("Ese Nombre No lo Conozco!! \nPrimero Tienes Que Registrarte, Mira La Opcion 1")
        time.sleep(2)
        return
    
    loading()

    print("\n¡Comencemos el juego!\n")

    ## DECLARACION DE VARIABLES
    puntuacion = 0
    puntosPorRespuesta = 0
    intentos = 0
    contador_de_acertijos  = 0
    equivocaciones = 0

    lista_de_acertijos = []
    lista_de_acertijos.extend(AcertijoFacil())
    lista_de_acertijos.extend(AcertijoMedio())
    lista_de_acertijos.extend(AcertijoDificil())

    for (i, acertijo) in enumerate(lista_de_acertijos):

        # intentos se reinicia cada que se hace una nueva pregunta
        if i < 3 :
            puntosPorRespuesta = 10

        elif i == 3 and i <= 5:
            puntosPorRespuesta = 20
            
        elif i == 6 and i <= 8:
            puntosPorRespuesta = 30

        print(f"Acertijo {i + 1}: {acertijo['pregunta']}")
        respuesta = input("Respuesta: ")

        if respuesta == acertijo['respuesta']:
            puntuacion += puntosPorRespuesta
            contador_de_acertijos += 1
            print( Emojis.CORRECT + "¡Respuesta correcta! Pasas al siguiente acertijo.\n")
            
        else:
            intentos += 1
            if intentos == 3:
                print("Tu respuesta no es correcta. Has excedido el número de intentos. termina tu partida...\n")
                break

            print( Emojis.ERROR + "Tu respuesta no es correcta, vuelve a intentarlo.\n")
            print(f"Acertijo {i + 1}: {acertijo['pregunta']}")

            respuesta = input("Respuesta: ")
            if respuesta == acertijo['respuesta']:
              puntuacion += puntosPorRespuesta
              contador_de_acertijos += 1
              print( Emojis.CORRECT + "¡Respuesta correcta! Pasas al siguiente acertijo.\n")

            else:   
              intentos += 1
              if intentos == 3:
                print("Tu respuesta no es correcta. Has excedido el número de intentos. termina tu partida...\n")
                break
              
              print( Emojis.ERROR + "Tu respuesta no es correcta, vuelve a intentarlo.\n")
              
              print(f"Acertijo {i + 1}: {acertijo['pregunta']}")
              respuesta = input("Respuesta: ")

              if respuesta == acertijo['respuesta']:
                puntuacion += puntosPorRespuesta
                contador_de_acertijos += 1
                print( Emojis.CORRECT + "¡Respuesta correcta! Pasas al siguiente acertijo.\n")

              else:
                intentos += 1
                
        if intentos == 3:
                print("Tu respuesta no es correcta. Has excedido el número de intentos. termina tu partida...\n")
                break

        ## falta un detalle en los intentos
        time.sleep(2)
        clear_output()
        os.system('cls')

    # AQUI DEBE HACER TODAS LAS VALIDACIONES QUE LA MAESTRA ESPECIFICA EN LA ULTIMA HOJA DEL PDF

    if contador_de_acertijos == 8 and equivocaciones == 0:
        puntuacion *= 2
    elif contador_de_acertijos == 8 and equivocaciones == 1:
        puntuacion += 30
    elif contador_de_acertijos == 8 and equivocaciones == 2:
        puntuacion += 25
    elif contador_de_acertijos == 7:
        puntuacion += 20
    elif contador_de_acertijos == 6:
        puntuacion += 15
    elif contador_de_acertijos == 5:
        puntuacion += 10
    elif contador_de_acertijos == 4:
        puntuacion -= 5
    elif contador_de_acertijos == 3:
        puntuacion -= 10
    elif contador_de_acertijos == 2:
        puntuacion -= 15
    elif contador_de_acertijos == 1:
        puntuacion = 1

    print(f"¡Acertaste { i } de 8 acertijos, tu puntuación final es {puntuacion}!")        

    registro_jugadores[existe_jugador['posicion']]['puntaje_partidas'].extend([puntuacion])
    registro_jugadores[existe_jugador['posicion']]['puntaje_total'] += puntuacion
    print(f"{registro_jugadores[existe_jugador['posicion']]['nombre']} tu nuevo puntaje es de {registro_jugadores[existe_jugador['posicion']]['puntaje_total']}")
    
    # al final de cada juego se ordena el ranking
    registro_jugadores.sort(key=lambda x: x['puntaje_total'], reverse=True)
    time.sleep(5)


def main():
    os.system('cls')
    clear_output()
    while True:
        mostrar_menu_principal()
        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            registrar_jugador()
        elif opcion == "2":
            verificar_puntuaciones()
        elif opcion == "3":
            jugar()
        elif opcion == "4":
            print("¡Buen día!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        
        loading()


def logo():
  os.system('cls')
  clear_output()
  print("\033[0;37m"+"████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""\033[0;36m"+"\n█████████████████████████░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████████████████""\033[0;34m"+"\n█████████████████████████░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████████████████""\033[0;32m"+"\n█████████████████████████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████████████████████████████""\033[0;33m"+"\n█████████████████████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████████████████""\033[0;31m"+"\n█████████████████████████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████████████████""\033[0;35m"+"\n█████████████████████████░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████████████████████████""\033[0;31m"+"\n█████████████████████████░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████████████████""\033[0;33m"+"\n█████████████████████████░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████████████████""\033[0;32m"+"\n█████████████████████████░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████████████████""\033[0;34m"+"\n█████████████████████████░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████████████████████████""\033[0;36m"+"\n█████████████████████████░░░░░░██████████░░░░░░█░░░░░░██░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░████████████████████████████""\033[0;37m"+"\n████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""\033[0;36m"+"\n█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░█████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█\n█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░▄▀░░░░░░█░░░░▄▀░░░░█████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█\n█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░███████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████\n█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░███████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█\n█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀░░███████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███████░░▄▀░░███████░░▄▀░░███░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█\n█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░███████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█\n█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█████░░▄▀░░█████░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█\n█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█\n█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████░░░░░░█████░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█\n█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
  print("UN PROGRAMA REGISTRADO BAJO EL DESARROLLO DE EQUIPOTEAM STUDIO 2023 © ")
  time.sleep(8)


logo()
main()