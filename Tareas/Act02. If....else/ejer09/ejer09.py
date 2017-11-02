import math
print ("Calculo de areas - Elija una figura geométrica: ")
print  ("a) Triangulo" )
print  ("b) Circulo" )
fig = input("¿Que figura quiere calcular?(Escriba t o c): ")
if fig == "c":
    radio = float(input("Escriba el radio: "))
    print ("Un circulo de radio %f tiene un area de %f" \
    % (radio, math.pi * (radio * radio) ))
elif fig == "t":
    base = float(input("Escriba la base: "))
    altura = float(input("Escriba la altura: "))
    print ("Un circulo de base %f y altura %f tiene un area de %.f3" \
    % (base, altura, base * altura / 2))#redondeo con el %.f2
else:
    print ("No es una opcion valida")