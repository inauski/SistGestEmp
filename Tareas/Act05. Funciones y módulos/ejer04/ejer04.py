print("Ejer 4")
num1 = int(input("Teclea un numero: "))
num2 = int(input("Teclea otro numero: "))

suma = lambda num1, num2: (num1 + num2)
print ("Suma: " ,suma(num1,num2))

resta = lambda num1,num2: (num1 - num2)
print ("Resta:" ,resta(num1,num2))

multi = lambda num1,num2: (num1 * num2)
print ("Multiplicacion: " ,multi(num1,num2))

div = lambda num1,num2: (num1 / num2)
print ("Division: ",div(num1,num2))
