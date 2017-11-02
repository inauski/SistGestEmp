from ejer02.ejer02 import ListaMinusMayus
# #rev
# dam2= ['SERGIO', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']
# numero = int(input("Nº a alumnos a consultar:"))
# for i in range(numero):
#     nom = input("Nombre a consultar: ").title()
#     veces = dam2.count(nom)
#     print("El nombre a consultar está:" , veces," veces")
#     cont = 0
#     j = 0
#     while cont < veces:
#         if dam2[j] == nom.title():
#             cont += 1
#             pos = j + 1
#             print("Posición " , pos)
#         j = j+ 1
#     print("\n")

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

l = ListaMinusMayus(lista)

numero = int(input("Nº alumnos a consultar:"))
for i in range(numero):
    nom = input("Nombre a consultar: ")
    print("Está en las posiciones", l.nombre_posiciones(nom))

