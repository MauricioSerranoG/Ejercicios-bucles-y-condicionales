"""
9.- Escribe un programa que pida una distancia en centímetros y que escriba esa
distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
"""

cm = float(input("Ingresa una distancia en cm --> "))
m = cm/100
km = m/1000
print(f"La medida en cm es: {cm}\nLa medida en m es: {m}\nLa medida en km es: {km}\n")

