"""

Crea un script llamado generador.py que cumpla las siguientes necesidades:

· Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. 
El objetivo es leer por pantalla un número >= que ini y <= que fin. Además a la hora de hacer la lectura se mostrará en el input el mensaje enviado a la función. 
Finalmente se devolverá el valor. Esta función tiene que devolver un número, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin).

· Una vez la tengas creada, deberás crear una nueva función llamada generador, no recibirá ningún parámetro. Dentro leerás dos números con la función leer_numero():
    - El primer numero será llamado numeros, deberá ser entre 1 y 20, ambos incluidos, y se mostrará el mensaje ¿Cuantos números quieres generar? [1-20]:
    - El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:.

· Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo siguiente:
    - Generarás una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
    - A cada uno de esos números deberás redondearlos en función de lo que el usuario ha especificado en el modo.
    - Para cada número muestra durante el redondeo, el número normal y después del redondeo.

· Finalmente devolverás la lista de números redondeados.

El objetivo de este ejercicio es  la reutilización de código y los módulos random y math.

"""

import random 
import math

class Nodo:
    def __init__(self, valor_original, valor_redondeado):
        self.valor_original = valor_original
        self.valor_redondeado = valor_redondeado
        self.siguiente = None

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if ini <= numero <= fin:
                return numero
            else:
                print(f"Por favor, ingrese un número entre {ini} y {fin}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    redondeo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    primer_nodo = None
    nodo_anterior = None

    for _ in range(numeros):
        num = random.uniform(0, 100)
        
        if redondeo == 1:
            redondeado = math.ceil(num)
        elif redondeo == 2:
            redondeado = math.floor(num)
        else:
            redondeado = round(num)

        nuevo_nodo = Nodo(num, redondeado)
        if primer_nodo is None:
            primer_nodo = nuevo_nodo
        else:
            nodo_anterior.siguiente = nuevo_nodo
        nodo_anterior = nuevo_nodo

    return primer_nodo

def imprimir_lista_numeros(nodo):
    while nodo is not None:
        print(f"Número original: {nodo.valor_original}, Número redondeado: {nodo.valor_redondeado}")
        nodo = nodo.siguiente

def imprimir_lista_numeros_redondeados(nodo):
    while nodo is not None:
        print(nodo.valor_redondeado)
        nodo = nodo.siguiente
    print("Fin de la lista.")

if __name__ == "__main__":
    lista_numeros = generador()
    print("Lista de números generados: ") 
    imprimir_lista_numeros(lista_numeros)
    print("Lista de números redondeados:")
    imprimir_lista_numeros_redondeados(lista_numeros)
