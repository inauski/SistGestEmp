import math
#MAL
print("Ecuacion de x2 + bx + c = 0")
a = int(input("Escriba el valor del coeficiente a: "))
b = int(input("Escriba el valor del coeficiente b: "))
c = int(input("Escriba el valor del coeficiente c: "))


if (a == b == 0):
    print ("Sin solucion " )
elif  (a == b == c == 0):
    print("Todos son solucion " )
elif (a == 0):
    print("Una solucion: " + str( -c / b))
else:
    x = (-b + math.sqrt( ( (b*b) - (4 * a * c) ) / (2 * a)))
    x1 = (-b - math.sqrt( ( (b*b) - (4 * a * c) ) / (2 * a)))
    print ("Las soluciones pueden ser " + str(x)+ " o " + str(x1))
