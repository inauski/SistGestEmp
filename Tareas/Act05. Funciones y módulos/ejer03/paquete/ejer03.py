print ("Ejer 4")
print("1. Área de un cuadrado")
print("2. Área de un triángulo")
opc = int(input("Teclea una opcion(1-2): ")) #mismates.leer_numero(mensaje) def leer_numero(mensaje) return input(mensaje)

if (opc == 1 ):
    lado = int(input("Dime el lado de un cuadrado: "))
    print("El area del cuadrado es: " + str(lado * lado))

if (opc == 2):
    base = int(input("Dime la base para el triangulo: "))
    alt = int (input("Dime la altura del triangulo: "))
    print("El area del triangulo es: " + str((base * alt) / 2))

tres = int(input("Teclea una texto:"))
print( int(tres), float(tres), str(tres))


