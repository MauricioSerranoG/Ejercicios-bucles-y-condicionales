"""
3. - Escribe un programa que pida dos números y que conteste cuál es el menor y
cuál el mayor o que escriba que son iguales.
"""
n1 = float(input("Ingresa el numero 1 --> "))
n2 = float(input("Ingresa el numero 2 --> "))
if n1 == n2:
    print("Los número son iguales")
elif n1 >n2:
    print(f"El número: {n1} es mayor, y el número: {n2} es el menor")
else:
    print(f"El número: {n2} es mayor, y el número: {n1} es el menor")



