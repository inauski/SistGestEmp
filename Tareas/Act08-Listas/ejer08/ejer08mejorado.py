from ejer02.ejer02 import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

l = ListaMinusMayus(lista)

borrar = input("Inserte el nombre a borrar: ")

listaNom = l.nombre_posiciones(borrar)

cont = 0
for pos in listaNom:
    a = input("Nombre encontrado en la posicion {}, desea borrarlo(s/n): ".format(pos))
    if a == "s" or a=="S":
        del l.lista[pos - cont]
        cont += 1
    elif a == "n" or a =="N":
        print ("No se ha borrado")
    else:
        print("Error")
print(lista)

