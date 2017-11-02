
print ("BAJAS")
dam2 = ["Sergio", "Xabi","Xabi", "Maria", "Alexander", "Carlos" ,"Juan" ,"Imanol", "Pedro" ,"Uxue", "Javier", "Iker", "Carlos", "Xabi", "Alejandra", "Carolina","Iñaki", "Asier","Maria"]
print (dam2)

nom = input("Nombre a eliminar: ")
nom= nom.capitalize()

while nom in dam2: #elimina los elementos repetidos de la lista
    if (dam2.count(nom)==0):
        print ('No se encuentra nombre')
    else:
        print ("El nombres aparece", dam2.count(nom), 'veces')
        dam2.remove(nom)
        print (dam2)


