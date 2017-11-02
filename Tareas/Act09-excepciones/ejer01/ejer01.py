while True:
    try:
        num = int(input("Teclea un numero entero "))
        break
    except ValueError:
        print("No es válido, ingrese un numero entero")