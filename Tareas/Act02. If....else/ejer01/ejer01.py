print("Divisor de números")
divd = int(input("Escriba el dividendo: "))
divs = int(input("Escriba el divisor: "))
if (divd % divs) == 0:
    print ("La division es exacta. Cociente " + str(divd//divs) )
elif (divd % divs) != 0:
    print ("La division no es exacta. Cociente " + str(divd // divs) + " Resto: " + str(divd % divs))
