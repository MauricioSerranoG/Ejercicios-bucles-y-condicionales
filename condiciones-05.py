"""
6.- Escribe un programa que pida los coeficientes de una ecuación de primer grado
(a x + b = 0) y escriba la solución.

Se recuerda que una ecuación de primer grado puede no tener solución, tener una
solución única, o que todos los números sean solución. Se recuerda que la fórmula
de las soluciones es x = -b / a
"""

a = float(input("Ingresa el valor de 'a' dentro de la excuacion tipo [a x + b = 0] --> "))
b = float(input("Ingresa el valor de 'b' dentro de la excuacion tipo [a x + b = 0] --> "))
if a == 0:
    print ("La ecuacion no tiene solución")
else:
    x = (-1*b)/a
    print(f"La solucion a la ecuacion es --> x = {x}")





