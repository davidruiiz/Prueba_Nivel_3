"""
Crea el siguiente módulo:
    · El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
    · En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
        - TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
        - ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado.

"""

def suma(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def resta(a, b):
    try:
        resultado = a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def producto(a, b):
    try:
        resultado = a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    return resultado

def division(a, b):
    try:
        resultado = a / b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
    return resultado