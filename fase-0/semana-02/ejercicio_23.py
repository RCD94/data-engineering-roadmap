try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()

    print(contenido)

except FileNotFoundError:
    print("El archivo no existe.")




"""try:
    # código que puede fallar
except FileNotFoundError:
    # qué hacemos si ocurre ese error"""



"""ValueError
    ↓
El dato tiene un formato incorrecto

FileNotFoundError
    ↓
El archivo que buscamos no existe"""