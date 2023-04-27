"""
Crea el siguiente módulo:
    · El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
    · En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
        - TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
        - ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado.

"""

class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        try:
            result= self.num1 + self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")

    def resta(self):
        try:
            result= self.num1 - self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")
    
    def producto(self):
        try:
            result= self.num1 * self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")

    def division(self):
        try:
            if self.num2==0:
                raise ZeroDivisionError
            result= self.num1 / self.num2
            return result
        except ZeroDivisionError:
            print("Error: División entre cero")
        except TypeError:
            print("Error: Tipo de dato no válido")

class Nodo:
    def __init__(self, operacion, siguiente=None):
        self.operacion = operacion
        self.siguiente = siguiente
    
    def obtener_operacion(self):
        print("La operación es: ", self.operacion)

    def obtener_siguiente(self):
        return self.siguiente
    
    def asignar_siguiente(self, siguiente):
        self.siguiente = siguiente

class ListaEnlazada: 
    def __init__(self):
        self.primero=None

    def esta_vacia(self):
        return self.primero==None
    
    def agregar(self, operacion):
        nuevo_nodo=Nodo(operacion)
        nuevo_nodo.asignar_siguiente(self.primero)
        self.primero=nuevo_nodo

    def eliminar(self):
        if self.primero==None:
            print("La lista está vacía")
            return None
        nodo_eliminado=self.primero
        self.primero=self.primero.obtener_siguiente()
        return nodo_eliminado.obtener_operacion()