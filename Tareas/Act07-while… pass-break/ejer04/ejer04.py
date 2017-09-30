#Escribir un programa que imprima los números pares que hay entre dos números introducidos por teclado

num1 = int(input("Introduce un número:  "))
num = num1
num2 = num1-1
resp = ""
while num > num2:
    num2 = int(input("Introduce otro número  "))
while num <= num2:
    if num % 2 == 0:
        resp = resp + "  " + str(num)
    num=num+1
print ("Numeros pares entre {} y {}".format(num1,num2))
print (resp)

