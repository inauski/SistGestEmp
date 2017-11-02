print("Comparador de multiplos")
num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba otro numero: "))
if ((num1 > num2) and ((num1 % num2)==0) ):
    print (str(num1) + " es multiplo de " + str(num2))
elif ((num2>num1) and ((num2 % num1)==0)):
    print(str(num2) + " es multiplo de " + str(num1))
elif ((num1 > num2) and ((num1 % num2)!=0) ):
    print(str(num1) + " no es multiplo de " + str(num2))
elif ((num2>num1) and ((num2 % num1)!=0)):
    print(str(num2) + " no es multiplo de " + str(num1))
elif ((num1==num2) and ((num2 % num1)==0)):
    print(str(num1) + " es multiplo de " + str(num2))