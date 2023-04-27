"""
Dada una pila de cartas de las cuales se conoce su número y palo, que representa un mazo de cartas de baraja española,resolver las siguientes actividades:
· generar las cartas del mazo de forma aleatoria;
· separar la pila mazo en cuatro pilas una por cada palo;
· ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
"""

import random

# Definición de la clase Carta
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return str(self.numero) + " de " + self.palo
    
class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x

    def pila_vacia(self):
        return self.cima is None

    def en_cima(self):
        if self.cima is not None:
            return self.cima.info
        else:
            return None

def generar_mazo():
    palos = ["espada", "basto", "copa", "oro"]
    mazo = Pila()

    cartas = [(palo, numero) for palo in palos for numero in range(1, 13) if numero != 8 and numero != 9]

    random.shuffle(cartas)

    for carta in cartas:
        mazo.apilar(carta)

    return mazo

def separar_por_palos(mazo):
    pilas_por_palo = {
        "espada": Pila(),
        "basto": Pila(),
        "copa": Pila(),
        "oro": Pila()
    }

    while not mazo.pila_vacia():
        carta = mazo.desapilar()
        pilas_por_palo[carta[0]].apilar(carta)

    return pilas_por_palo

def ordenar_pila(pila):
    pila_ordenada = Pila()
    while not pila.pila_vacia():
        carta = pila.desapilar()
        temp = Pila()

        while not pila_ordenada.pila_vacia() and pila_ordenada.en_cima()[1] < carta[1]:
            temp.apilar(pila_ordenada.desapilar())

        pila_ordenada.apilar(carta)

        while not temp.pila_vacia():
            pila_ordenada.apilar(temp.desapilar())

    return pila_ordenada

def main():
    mazo = generar_mazo()
    pilas_por_palo = separar_por_palos(mazo)
    pila_ordenada = ordenar_pila(pilas_por_palo["basto"])

    while not pila_ordenada.pila_vacia():
        carta = pila_ordenada.desapilar()
        print(carta)

if __name__ == '__main__':
    main()