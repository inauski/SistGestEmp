from ejer02 import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

l = ListaMinusMayus(lista)

nombre = input("Nombre a buscar: ")
print("Está en las posiciones", l.nombre_posiciones(nombre))


