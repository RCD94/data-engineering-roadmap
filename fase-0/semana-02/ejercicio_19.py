with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip() for linea in lineas]
productos = [producto.split(",") for producto in lineas]
nombres = [producto[0] for producto in productos if int(producto[1]) > 50]
print(nombres)