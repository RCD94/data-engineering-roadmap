productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Monitor", "precio": 150}
]

precios = {
    producto["nombre"]:
    producto["precio"]
    for producto in productos
}

print(precios)