"""
2.- Mejora el programa anterior haciendo que tenga en cuenta que no se puede
dividir por cero."""

num1 = float(input("Ingresa el numero 1 (dividendo)--> "))
num2 = float(input("Ingresa el numero 2 (divisor)--> "))
while num2 == 0:
    print("ERROR, el divisor no puede valer cero: ")
    num2 = float(input("Ingresa el numero 2 (divisor)--> "))

residuo = float(num1%num2)
if residuo == 0:
    print(f"La division es exacta, pues su residuo es de: {residuo}")
else:
    print(f"La division no es exacta, pues su residuo es de: {residuo}")