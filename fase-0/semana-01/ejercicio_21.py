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

valor_total = 0

for producto in productos:
    precio_por_stock = producto["precio"] * producto["stock"]
    valor_total += precio_por_stock
    print(f"{producto['nombre']} -> {producto['precio']} * {producto['stock']} = {precio_por_stock}€")

print(f"Valor total del inventario: {valor_total}€")