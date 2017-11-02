lista = dict()

lista= {('Ana', 'correo1@ana.es', 'correo2@ana.es','Ana', 'correo3@ana.es', 'correo4@ana.es','Ana', 'correo5@ana.es'), ('Maria', 'correo1@maria.es'), ('Iker', 'correo1@iker.es',"correo'2@iker.es")}

# for elem in range(len(lista)):
#     print(elem,lista[elem])
futbolistas = dict()

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
values = futbolistas.values()
print("\nValores del diccionario futbolistas.values(): \n%s"%values)

# for c,v in enumerate(['ta', 'te', 'ti']):
#      print(c, " : ",v)