"""
4.- Escribe un programa que pida dos números enteros y que escriba si el mayor es
múltiplo del menor.
"""
n1 = float(input("Ingresa el numero 1 --> "))
n2 = float(input("Ingresa el numero 2 --> "))
if n1 == n2:
    print("Los número son iguales")
elif n1 >n2:
    print(f"El número: {n1} es mayor, y el número: {n2} es el menor")
    multiplo = n1 % n2
    if multiplo == 0:
        print(f"El numero {n1}, es multiplo de: {n2}")
    else:
        print(f"{n1}, no es multiplo de {n2}")
else:
    print(f"El número: {n2} es mayor, y el número: {n1} es el menor")
    multiplo = n2 % n1
    if multiplo == 0:
        print(f"El numero {n2}, es multiplo de: {n1}")
    else:
        print(f"{n2}, no es multiplo de {n1}")