
op = int(input("Dime un numero: "))
if op < 1:
    print("Imposible")
else:
    lista = []
    for i in range(op):
        palabra = input("Nombre %s : " % str(i + 1))
        lista += [palabra]
    print("La lista creada es:", lista)







