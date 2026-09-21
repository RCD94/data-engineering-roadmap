with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

productos = [linea.strip() for linea in lineas]

print(len(productos))