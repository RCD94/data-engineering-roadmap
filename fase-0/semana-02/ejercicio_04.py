def calcular_total(precio, cantidad):
    return precio * cantidad

def calcular_precio_final(precio, descuento):
    porcentaje = (precio * descuento) / 100
    return precio - porcentaje

total = calcular_total(50, 3)
precio_final = calcular_precio_final(total, 10)

print(precio_final)