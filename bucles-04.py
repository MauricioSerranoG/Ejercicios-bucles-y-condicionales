"""
4.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números y escriba cuántos negativos ha introducido.
"""

contador = 0
cantidad = int(input("¿Cuantos numeros deseas ingresar? --> "))
while contador < cantidad:
    siguiente = float(input(f"Ingresa el numero {contador + 1} --> "))
    if  siguiente < 0:
         print(f"El primer numero [{siguiente}] es un numero negativo\n")
         contador += 1
    else:
        print(f"El primer [{siguiente}], es un positivo\n")
        contador += 1

