import random
#clase juego
class Gusano:
    def __init__(self):
        self.posicion = [0,0]
        self.cuerpo = ["■"]
        self.tablero = []
        self.comida = []
        self.puntuacion = 0
        self.crear_tablero()
        self.crear_comida()
        self.crear_gusano()
        self.mover_gusano()
    
def crear_tablero(self):
    for i in range(10):
        tablero.append(["O"]*10)
    return tablero

def crear_comida(self):
    self.comida = ["✩"]
    posicion_comida = [random.randint(0,9), random.randint(0,9)]
    self.tablero[posicion_comida[0]][posicion_comida[1]] = self.comida

def crear_gusano(self):
    self.tablero[self.posicion[0]][self.posicion[1]] = self.cuerpo

def main(self):
    print("="*50)
    print(Font.renderText('Culebrita'))
    print("="*50)
    while True:
        for i in range(10):
            print(" ".join(self.tablero[i]))
        print("="*50)
        print("")

if __name__ == "__main__":
    main(Gusano())