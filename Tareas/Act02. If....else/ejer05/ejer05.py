print("Comparador de 3 numeros")
num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro numero: "))
num3 = int(input("Escriba otro numero mas"))
if (num1 == num2 and num1 == num3):
    print ("Ha escrito tres veces el mismo numero " )
elif  (num1 == num2 and num1 != num3 or num1==num3 and num1 != num2):
    print("Ha escrito uno de los numeros dos veces " )
else:
    print("Son los 3 distintos")
