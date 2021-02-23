"""
7.-Escribe un programa que contenga una función que reciba los coeficientes de
una ecuación de segundo grado (a x2 + b x + c = 0) y retorne la solución.
Se recuerda que una ecuación de segundo grado puede no tener solución, tener
una solución única, tener dos soluciones o que todos los números sean solución. Se
recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ±
√(b2
-4ac) ) / (2a)
Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no
tiene por qué corresponder con el orden de las condiciones).
"""
import math

def evaluador(a, b, c):
    discriminante = (b**2)-4*a*c
    return discriminante


print("Ecuaciones de segundo grado tipo: (ax^2 + bx + c = 0)")
a = float(input("Ingresa el valor de a --> "))
b = float(input("Ingresa el valor de b --> "))
c = float(input("Ingresa el valor de c --> "))
soluciones = evaluador(a, b, c)

if soluciones > 0:
    resultado1 = ((-1*b) + math.sqrt(soluciones))/(2*a)
    resultado2 = ((-1*b) - math.sqrt(soluciones))/(2*a)
    print(f"Las soluciones son x1 = {resultado1}, x2 = {resultado2}")
if soluciones == 0:
    resultado1 = ((-1*b) + math.sqrt(soluciones))/(2*a)
    print(f"La unica solucion es x = {resultado1}")
    #Tiene una solucion aplicar F.G a las 1 variables
elif soluciones < 0 or a == 0:
    print("Esta ecuacion no tiene soluciones reales")


"""
20460545-Ejercicios-Python
Ejercicios-03
condiciones-05.py
"""

