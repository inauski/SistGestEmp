def leernumero(num):
    try:
        return int(num)
    except ValueError as err:
        raise ValueError("No es válido, ingrese un numero entero")


while True:
    num = input("Teclea un número entero: ")
    try:
        print(leernumero(num))
        break
    except ValueError as err:
        print(err)

