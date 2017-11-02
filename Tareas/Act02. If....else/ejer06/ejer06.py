print("Comprobador de años bisiestos")
num1 = int(input("Escriba un año y le dire si es bisiesto: "))
#MAL
if (num1 % 4 != 0 ):
    print ("El año  no es bisiesto " )
elif  (num1 % 100 == 0 and num1 % 400 !=0 ):
    print("El año "+ str(num1) + " no es bisiesto porque es multiplo de 100 pero no de 400 " )
elif (num1 % 4 == 0 and num1 % 100 !=0 ):
    print("El año " + str(num1) + " es bisiesto")
else:
    print ("El año " + str(num1) +" es bisiesto porque es múltiplo de 400")

