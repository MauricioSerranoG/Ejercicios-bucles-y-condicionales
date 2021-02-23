"""
5.- Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números, y escriba el mayor, el menor y la media aritmética.
Se recuerda que la media aritmética de un conjunto de valores es la suma de esos
valores dividida por la cantidad de valores.
"""
numero = []
contador = 0
mayor = 0
menor = 1
cantidad = int(input("¿Cuantos numeros deseas ingresar? --> "))
while contador < cantidad:
    siguiente = float(input("Ingresa el siguiente numero --> "))
    if siguiente >= mayor:
        mayor = siguiente
    if siguiente <= menor:
        menor = siguiente
    numero.append(siguiente)
    contador += 1

print("Lista de numeros: ", numero[:])
print(f"El numero mayor es: {mayor}\nEl numero menor es {menor}")