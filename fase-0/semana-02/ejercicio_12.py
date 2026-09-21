productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Monitor", "precio": 150},
    {"nombre": "Webcam", "precio": 80}
]

productos_caros = [producto for producto in productos if producto["precio"] > 50]

print(productos_caros)