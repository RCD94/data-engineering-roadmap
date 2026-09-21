try:
    numero = int(input("Introduce un número: "))
    print(f"Has introducido: {numero}")
except ValueError:
    print("Eso no es un número válido.")