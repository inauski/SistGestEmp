print("Comparador de números")
num1 = float(input("Escriba un numero: "))
num2 = float(input("Escriba otro numero: "))
if (num1 > num2):
    print ("Menor: " + str(num2)+ " ; Mayor " + str(num1) )
elif  (num2 > num1):
    print("Menor: " + str(num1) + " ; Mayor " + str(num2))
elif (num2 == num1):
    print ("Los numeros son iguales")