with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip() for linea in lineas]
productos = [producto.split(",") for producto in lineas]

total = 0

for producto in productos:
    total += int(producto[1])

print(f"Valor total: {total}€")