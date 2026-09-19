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
    print(f"Nombre: {producto['nombre']} | Precio: {producto['precio']}€ | Stock: {producto['stock']}")