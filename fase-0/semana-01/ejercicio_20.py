productos = [
    {
        "nombre": "Teclado",
        "precio": 25,
        "stock": 10
    },
    {
        "nombre": "Ratón",
        "precio": 15,
        "stock": 20
    },
    {
        "nombre": "Monitor",
        "precio": 150,
        "stock": 5
    }
]

for producto in productos:
    if producto["stock"] < 10:
        print(f"Producto: {producto['nombre']} | Stock: {producto['stock']}")