print("Comparador de multiplos")
num1 = int(input("En que año estamos?: "))
num2 = int(input("Escriba un año cualquiera: "))
if (num1 < num2):
    print ("Para llegar al año " + str(num2) + " faltan " + str(num2-num1)+ " años" )
elif  (num1 > num2):
    print("Han pasado: " + str(num1-num2) + " años")
elif (num2 == num1):
    print ("Son el mismo año")

