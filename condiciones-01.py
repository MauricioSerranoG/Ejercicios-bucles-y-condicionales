"""
1.- Escribe un programa que pida dos números enteros y que calcule su división,
escribiendo si la división es exacta o no."""

num1 = float(input("Ingresa el numero 1 --> "))
num2 = float(input("Ingresa el numero 2 --> "))
residuo = float(num1%num2)
if residuo == 0:
    print(f"La division es exacta, pues su residuo es de: {residuo}")
else:
    print(f"La division no es exacta, pues su residuo es de: {residuo}")