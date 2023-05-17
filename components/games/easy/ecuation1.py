## this is just a example
from components.games.points import easyPoints
from components.games.points import failPoints

def ecuation1():
    try:
        expectedResult = 4

        print("Cuál es el valor de 'x' cuado '4 + x = 8'")
        result = int(input())

        if(result == expectedResult): return easyPoints

        return failPoints

    except:
        print(f"Mal, el valor debe ser númerico, la respuesta correta es: {expectedResult}")
        return failPoints
