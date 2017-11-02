print("Ecuacion de x + b = 0")
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
if (a == b ==0):
    print ("Todas las respuestas son solucion " )
elif  (a == 0):
    print("No tiene solucion " )
else:
    print("La ecuacion tiene una solucion " + str(-b / a))
