"""
2.- Escriba un programa que pida un número entero mayor que cero y que escriba
sus divisores.
"""
contador = 1
numero = int(input("Ingresa un numero entero mayor que cero --> "))
while numero < 0:
    numero = int(input("Ese valor no es valido, ingresa otro --> "))
print("CALCULANDO DIVISORES...\n")
while contador <100:
    if numero%contador == 0:
        print(f"El numero {contador}, es divisor de {numero}")
    contador += 1
