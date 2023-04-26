"""
El gran almirante del MCU Khan “El Conquistador” es el estratega del multiverso y normalmente se encuentra desbordado de pedidos de sugerencia de cómo actuar por las variantes de el mismo de las diferentes épocas y Multiversos.
Para lo cual nos solicita desarrollar un algoritmo que le permita atender los pedidos de ayuda de acuerdo con la prioridad de los mismo en base a los siguientes requerimientos:
 
a. se deben contemplar tres niveles de prioridad para la cola;
b. cada pedido de sugerencia cuenta con la siguiente información: nombre del “Khan” solicitante, multiverso en el que se encuentra o el más próximo y descripción del pedido;
c. aquellos pedidos que provengan del “Gran Conquistador”, del universo de 616 o la descripción mencione a “El que permanece” tendrán la mayor prioridad;
d. si el pedido es del “Khan que todo lo sabe” o la descripción menciona “Carnicero de Dioses” o universo “838” tendrán prioridad media;
e. el resto de los pedidos serán de prioridad baja;
f. realizar la atención de la cola almacenando los pedidos de mayor prioridad en una pila llamada “bitácora” para revisión y seguimiento;
g. luego de cada atención se podrá agregar un pedido a la cola.

"""


class Heap(object):

    """Crea un montículo"""

    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1

    def quitar(self):
        self.intercambio(0, self.tamanio-1)
        dato = self.vector[self.tamanio-1]
        self.tamanio -= 1
        self.hundir(0)
        return dato

    def heap_vacio(self):
        return self.tamanio == 0

    def flotar(self, indice):
        while(indice > 0 and self.vector[indice] > self.vector[(indice - 1) // 2]):
            padre = (indice - 1) // 2
            self.intercambio(indice, padre)
            indice = padre

    def hundir(self, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if self.vector[hijo_der] > self.vector[hijo_izq]:
                    aux = hijo_der
            if (self.vector[indice] < self.vector[aux]):
                self.intercambio(indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()[1]

    def intercambio(self, indice1, indice2):
        self.vector[indice1], self.vector[indice2] = self.vector[indice2], self.vector[indice1]

class nodoPila(object):

    """Clase nodo pila"""

    info, sig = None, None

class Pila(object):
    
    """Clase Pila"""

    def __init__(self):
        self.tamanio = 0
        self.tope = None

    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.tope
        self.tope = nodo
        self.tamanio += 1

    def desapilar(self):
        dato = self.tope.info
        self.tope = self.tope.sig
        self.tamanio -= 1
        return dato

    def pila_vacia(self):
        return self.tope is None

    def tamanio_pila(self):
        return self.tamanio

    def elemento_cima(self):
        return self.tope.info

    def mover(self, origen, destino):
        dato = origen.desapilar()
        destino.apilar(dato)

    def barrido_pila(self):
        pila_aux = Pila()
        while(not self.pila_vacia()):
            dato = self.desapilar()
            print(dato)
            pila_aux.apilar(dato)
        while(not pila_aux.pila_vacia()):
            dato = pila_aux.desapilar()
            self.apilar(dato)

def prioridad(pedido):
    nombre, multiverso, descripcion = pedido
    if (nombre == "Gran Conquistador" or multiverso == "616" or "El que permanece" in descripcion):
        return 1
    elif (nombre == "Kang que todo lo sabe" or "Carnicero de Dioses" in descripcion or multiverso == "838"):
        return 2
    else:
        return 3

def procesar_pedidos(pedidos):
    max_tam_heap = len(pedidos)
    heap = Heap(max_tam_heap)
    bitacora = Pila()

    for pedido in pedidos:
        prioridad_pedido = prioridad(pedido)
        heap.arribo(pedido, prioridad_pedido)

    while not heap.heap_vacio():
        pedido_atendido = heap.atencion()
        bitacora.apilar(pedido_atendido)

    return bitacora

def main():
    pedidos = [
        ("Centurión Escarlata", "712", "Ayuda con el Carnicero de Dioses"),
        ("Gran Conquistador", "616", "Estrategia para detener a El que permanece"),
        ("Rama-Tut", "700089", "Defensa contra invasión interdimensional"),
        ("Nathaniel Richards", "838", "Busco asesoramiento sobre cómo proteger mi planeta"),
        ("Iron Lad", "6311", "Necesito ayuda para encontrar un objeto perdido")
    ]

    bitacora = procesar_pedidos(pedidos)

    print("Bitácora de pedidos atendidos:")
    while not bitacora.pila_vacia():
        print(bitacora.desapilar())

if __name__ == "__main__":
    main()
