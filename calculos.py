"""
Crea el siguiente módulo:
    · El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. Todas ellas devolverán el resultado.
    · En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
        - TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
        - ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el módulo y realizar las siguientes instrucciones. Observa si el comportamiento es el esperado.

"""

from operaciones import *
 

operacion1=Operaciones(10, 5)
operacion2=Operaciones(5, "hola")
operacion3=Operaciones(5, 5) 
operacion4=Operaciones(10, 0)

lista=ListaEnlazada()

resultado_suma=operacion1.suma()
resultado_resta=operacion2.resta()
resultado_producto=operacion3.producto()
resultado_division=operacion4.division()

print("{} + {} = {}".format(operacion1.num1, operacion1.num2, resultado_suma))
print("{} - {} = {}".format(operacion2.num1, operacion2.num2, resultado_resta))
print("{} * {} = {}".format(operacion3.num1, operacion3.num2, resultado_producto))
print("{} / {} = {}".format(operacion4.num1, operacion4.num2, resultado_division))


