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

while True:
    print("===== GESTOR DE PRODUCTOS =====")
    print("1. Mostrar productos")
    print("2. Añadir producto")
    print("3. Buscar producto")
    print("4. Productos con poco stock")
    print("5. Valor total del inventario")
    print("6. Salir")
    print("")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        for producto in productos:
            print(f"{producto['nombre']} - {producto['precio']}€ - Stock: {producto['stock']}")
        print("")
    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Stock del producto: "))
        nuevo_producto = {"nombre": nombre, "precio": precio, "stock": stock}
        productos.append(nuevo_producto)
        print("")
    elif opcion == "3":
        nombre_buscar = input("Nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto["nombre"] == nombre_buscar:
                print(f"{producto['nombre']} - {producto['precio']}€ - Stock: {producto['stock']}")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")
        print("")
    elif opcion == "4":
        encontrado = False
        for producto in productos:
            if producto["stock"] < 10:
                print(f"{producto['nombre']} - {producto['precio']}€ - Stock: {producto['stock']}")
                encontrado = True
        if not encontrado:
            print("No hay productos con poco stock.")
        print("")
    elif opcion == "5":
        valor_total = 0
        for producto in productos:
            valor = producto['precio'] * producto['stock']
            valor_total += valor
        print(f"Valor total del inventario: {valor_total}")
        print("")
    elif opcion == "6":
        print("Saliendo del gestor de productos...")
        break
    else:
        print("Opción no válida.")
