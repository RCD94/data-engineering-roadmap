productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Monitor", "precio": 150},
    {"nombre": "Webcam", "precio": 80}
]

nombres = [producto["nombre"] for producto in productos]

print(nombres)