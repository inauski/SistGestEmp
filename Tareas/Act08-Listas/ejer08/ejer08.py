print ("BAJAS")
dam2 = ["Sergio", "Xabi","Xabi", "Maria", "Alexander", "Carlos" ,"Juan" ,"Imanol", "Pedro" ,"Uxue", "Javier", "Iker", "Carlos", "Xabi", "Alejandra", "Carolina","Iñaki", "Asier","Maria"]
print (dam2)

nom = input("Nombre a eliminar: ")
nom= nom.capitalize()


print ("El nombres aparece " + str(dam2.count(nom)) + ' veces')

#no imprime bien la pos buscada
for i in range(0, dam2.count(nom)):
    pos = dam2.index(nom)
    resp = input(nom + ' esta en la posicion  ' + str(pos) + ' --> ¿Quieres borrarlo?(S/N)')

    if resp == 'S' or resp == 's':
        dam2.pop(pos)
    elif resp =='N' or resp == 'n':
        print("No se ha borrado")
    else:
        print("Error")
print (dam2)
