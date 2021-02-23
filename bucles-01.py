"""
1.- Escribe una función que reciba una lista de 6 números enteros ingresados por
teclado e imprima cuales son pares, impares y a su vez si son primos o no.
al final retorna la suma de todos los números.
"""
import math
numeros = [10, 5, 8, 9, 40, 27]

def analizador (lista):
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            print(f"El valor {lista[i]}, es un par")
        else:
            print(f"El valor {lista[i]}, es un inpar")


print("Lista de numeros = ", numeros[:])
analizador(numeros)

