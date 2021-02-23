"""
8.- Escribe un programa que pregunte primero si se quiere calcular el área de un
triángulo o la de un círculo. 

Si se contesta que se quiere calcular el área de un
triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura
y escribir el área. 

Si se contesta que se quiere calcular el área de un círculo
(escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el
área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
Nota: Utilice como valor de pi el valor 3.141592.
"""
"""
20460545-Ejercicios-Python
Ejercicios-03
condiciones-05.py
"""

import math

op = (input("¿Deceas calcular el area de un triangulo o de un circulo? --> "))
if op == "Triangulo" or op == "triangulo":
    base = float(input("Ingresa la medida de la base del triangulo --> "))
    altura = float(input("Ingresa la altura de la base del triangulo --> "))
    area_t = (base * altura)/2
    print(f"El area del triangul es: {area_t}")
elif op == "Circulo" or op == "circulo":
    radio = float(input("Ingresa el radio del Circulo --> "))
    area_c = math.pi*(radio**2)
    print(f"El area del circulo es: {area_c}")
else:
    print("Esa opcion no existe, saliendo...")