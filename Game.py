import random
from pyfiglet import Figlet # Librery = pip install pyfiglet==0.7
Font = Figlet(font='slant') # Fuente del título

def main(buscar_comida, tablero, culebrita, comida, mover_culebrita): # Función principal
    print("="*50)
    print(Font.renderText('Culebrita')) # Imprimir el título
    print("="*50)
    tablero = tablero()
    comida(tablero)
    culebrita = culebrita()
    lista_culebrita = [] # Lista para guardar la posición de la culebrita
    longitud_culebrita = 1 # Longitud de la culebrita
    while True:
        mover_culebrita(culebrita, comida, tablero) # Llamar a la función mover_culebrita
        
        cabeza_culebrita = [posicion_actual[0], posicion_actual[1]] # Posición de la cabeza de la culebrita
        lista_culebrita.append(cabeza_culebrita) # Agregar la posición de la cabeza de la culebrita a la lista

        if len(lista_culebrita) > longitud_culebrita: # Si la longitud de la lista es mayor a la longitud de la culebrita
            del lista_culebrita[0] # Eliminar el primer elemento de la lista

        for i in range(len(lista_culebrita)): # Recorrer la lista
            tablero[lista_culebrita[i][0]][lista_culebrita[i][1]] = culebrita # Agregar la posición de la culebrita en el tablero

        if buscar_comida(posicion_actual, posicion_comida) == True: # Si la posición actual es igual a la posición de la comida
            comida(tablero) # Agregar comida
            longitud_culebrita += 1    # Aumentar la longitud de la culebrita
            print(lista_culebrita) # Imprimir la lista
            print(longitud_culebrita) # Imprimir la longitud de la culebrita
        

        for i in range(10): # Recorrer el tablero
            print(" ".join(tablero[i])) # Imprimir el tablero
        print("="*50) # Separador
        print("")


def buscar_comida(posicion_actual, posicion_comida): # Función para buscar la comida
    if posicion_actual == posicion_comida:
        return True

def culebrita(): 
    culebrita = ("■")
    return culebrita

def comida(tablero):
    global posicion_comida 
    comida = ("✩")
    posicion_comida = [random.randint(0, 9), random.randint(0, 9)] # Posición de la comida
    tablero[posicion_comida[0]][posicion_comida[1]] = comida # Agregar la comida en el tablero


def tablero():
    tablero = [] # Lista para guardar el tablero
    for i in range(10): # Recorrer el tablero
        tablero.append(["O"]*10) # Agregar "O" en el tablero
    return tablero


def mover_culebrita(culebrita, comida, tablero):
    global posicion_actual  # Variable global
    mover_culebrita = input("¿Dónde quieres mover la culebrita? (W, A, S, D): ")
    posicion_actual = [0, 0] # Posición actual de la culebrita
    for i in range(10): # Recorrer el tablero en el eje Y
        for j in range(10): # Recorrer el tablero en el eje X
            if tablero[i][j] == culebrita: # Si el tablero en la posición i, j es igual a la culebrita
                posicion_actual = [i, j] # Posición actual de la culebrita

    if mover_culebrita == "w" or mover_culebrita == "W": # Si la tecla presionada es W
        if posicion_actual[0] == 0: # Si la posición actual en el eje Y es igual a 0
            print("No puedes salirte del tablero") # Imprimir mensaje
        else: # Si no
            tablero[posicion_actual[0]][posicion_actual[1]] = "O" # Agregar "O" en la posición actual de la culebrita
            tablero[posicion_actual[0]-1][posicion_actual[1]] = culebrita # Agregar la culebrita en la posición actual - 1

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



if __name__ == "__main__": # Si el archivo se ejecuta directamente
    main(buscar_comida, tablero, culebrita, comida, mover_culebrita) # Ejecutar la función main
