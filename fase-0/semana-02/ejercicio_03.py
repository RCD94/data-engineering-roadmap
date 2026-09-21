def calcular_precio_final(precio, descuento):
    porcentaje = (precio * descuento) / 100
    return precio - porcentaje

resultado = calcular_precio_final(100, 20)
print(resultado)