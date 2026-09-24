try:
    with open("ventas.txt", "r") as archivo:
        lineas = archivo.readlines()

    def calcular_total(precio, cantidad):
        return precio * cantidad

    ingresos_totales = 0
    lineas_limpias = [linea.strip() for linea in lineas]
    lista_productos = [linea.split(",") for linea in lineas_limpias]
    ventas_analizadas = len(lista_productos)
    mayor_ingreso = 0
    producto_mayor_ingreso = ""
    datos_ventas = []
    suma_precios = 0

    for producto in lista_productos:
        datos = {
            "producto": producto[0],
            "precio": int(producto[1]),
            "cantidad": int(producto[2]),
            "ingresos": calcular_total(int(producto[1]), int(producto[2])),
        }
        datos_ventas.append(datos)

    for dato in datos_ventas:
        ingresos_totales += dato["ingresos"]
        suma_precios += dato["precio"]
        if dato["ingresos"] > mayor_ingreso:
            mayor_ingreso = dato["ingresos"]
            producto_mayor_ingreso = dato["producto"]

    productos_mas_100 = [dato for dato in datos_ventas if dato["ingresos"] > 100]

    precio_medio_productos = suma_precios / ventas_analizadas

    with open("resumen_ventas.txt", "w") as archivo:
        archivo.write("RESUMEN DE VENTAS\n")
        archivo.write("=================\n")
        archivo.write(f"Ventas analizadas: {ventas_analizadas}\n")
        archivo.write(f"Ingresos totales: {ingresos_totales}€\n")
        archivo.write(f"Precio medio: {precio_medio_productos:.2f}€\n")
        archivo.write("\n")
        archivo.write("Producto con mayores ingresos:\n")
        archivo.write(f"{producto_mayor_ingreso}\n")
        archivo.write("\n")
        archivo.write(f"Ingresos: {mayor_ingreso}€\n")
        archivo.write("\n")
        archivo.write(f"Productos con ingresos superiores a 100€:\n")

        for dato in productos_mas_100:
            archivo.write(f"{dato['producto']} -> {dato['ingresos']}€\n")

except FileNotFoundError:
    print("El archivo no existe.")

except ValueError:
    print("Hay un precio que no es válido.")