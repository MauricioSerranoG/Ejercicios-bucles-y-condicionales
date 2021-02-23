"""
3.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números, y muestre un mensaje cada vez que un número no sea mayor que el
primero.
""" 
contador = 0
cantidad = int(input("¿Cuantos numeros deseas ingresar? --> "))
primero = float(input("Ingresa el primer numero --> "))
while contador < cantidad:
    siguiente = float(input("Ingresa el siguiente numero --> "))
    if primero > siguiente:
         print(f"El primer numero [{primero}] es mayor que [{siguiente}]\n")
         contador += 1
    else:
        print(f"El primer numero [{primero}] es menor que [{siguiente}]\n")
        contador += 1