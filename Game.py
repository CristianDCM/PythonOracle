#Librery = pip install pyfiglet==0.7
import random
from pyfiglet import Figlet
Font = Figlet(font='slant')

def main(buscar_comida,tablero, culebrita, comida, mover_culebrita):
    print("="*50)
    print(Font.renderText('Culebrita'))
    print("="*50)
    tablero = tablero()
    comida(tablero)
    culebrita = culebrita()
    longitud_culebrita = []
    while True:        
        mover_culebrita(culebrita, comida, tablero)
        if buscar_comida(posicion_actual, posicion_comida) == True:
            comida(tablero)
            #Arreglar aumento de longitud de la culebrita
            longitud_culebrita.append(culebrita)
            total = len(longitud_culebrita)
            print("Puntuación: ", total)
            if total > 0:
                print(longitud_culebrita)
    
        for i in range(10):
            print(" ".join(tablero[i]))
        print("="*50)
        print("")

def buscar_comida(posicion_actual, posicion_comida):
    if posicion_actual == posicion_comida:
        return True

def culebrita():
    culebrita = ("■")
    return culebrita

def comida(tablero):
    global posicion_comida
    comida = ("✩")
    posicion_comida = [random.randint(0,9), random.randint(0,9)]
    tablero[posicion_comida[0]][posicion_comida[1]] = comida
    
def tablero ():
    tablero = []
    for i in range(10):
        tablero.append(["O"]*10)
    return tablero

def mover_culebrita(culebrita, comida, tablero):
    global posicion_actual
    mover_culebrita = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    posicion_actual = [0,0]
    for i in range(10):
        for j in range(10):
            if tablero[i][j] == culebrita:
                posicion_actual = [i, j]
    
    if mover_culebrita == "w" or mover_culebrita == "W":
        if posicion_actual[0] == 0:
            print("No puedes salirte del tablero")
        else:
            tablero[posicion_actual[0]][posicion_actual[1]] = "O"
            tablero[posicion_actual[0]-1][posicion_actual[1]] = culebrita

    elif mover_culebrita == "a" or mover_culebrita == "A":
        if posicion_actual[1] == 0:
            print("No puedes salirte del tablero")
        else:
            tablero[posicion_actual[0]][posicion_actual[1]] = "O"
            tablero[posicion_actual[0]][posicion_actual[1]-1] = culebrita

    elif mover_culebrita == "s" or mover_culebrita == "S":
        if posicion_actual[0] == 9:
            print("No puedes salirte del tablero")
        else:
            tablero[posicion_actual[0]][posicion_actual[1]] = "O"
            tablero[posicion_actual[0]+1][posicion_actual[1]] = culebrita

    elif mover_culebrita == "d" or mover_culebrita == "D":
        if posicion_actual[1] == 9:
            print("No puedes salirte del tablero")
        else:
            tablero[posicion_actual[0]][posicion_actual[1]] = "O"
            tablero[posicion_actual[0]][posicion_actual[1]+1] = culebrita    
    return posicion_actual

if __name__ == "__main__":
    main(buscar_comida,tablero, culebrita, comida, mover_culebrita)