
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
    if (nombre == "Gran conquistador" or multiverso == "616")
    