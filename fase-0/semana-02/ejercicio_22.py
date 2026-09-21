nombre = input("Nombre: ")

try:
    precio = int(input("Precio: "))
    stock = int(input("Stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    print(producto)

except ValueError:
    print("El precio y el stock deben ser números.")