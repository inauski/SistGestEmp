class ListaMinusMayus:
    lista =[]
    def __init__(self, lista):
        self.lista = lista
    def a_minus(self):
        dam2_min = []
        for i in (self.lista):
            dam2_min.append(i.lower())
        return dam2_min
    def a_mayus(self):
        dam2_mayus = []
        for i in (self.lista):
            dam2_mayus.append(i.upper())
        return dam2_mayus
    def a_title(self):
        dam2_title = []
        for i in (self.lista):
            dam2_title.append(i.capitalize())
        return dam2_title
    def cuenta_nombre(self,nombre):
        #cont=0
        #for i in self.lista:
            #if i.lower() == buscar.lower():
                #cont +=1
        #print("Lista: ", cont)
        self.a_minus()
        return self.lista.count(nombre.lower())

    def nombre_posiciones(self, buscar):
        posic = []
        for i in range(len(self.lista)):
            if self.lista[i].lower() == buscar.lower():
                posic.append(i)
        if len(posic) == 0:
            return bool(0)
        else:
            return posic


lista = ["Beñat", "Xabi", "Xabi", "María", "Alexander", "Carlos", "Juan", "Imanol", "Pedro", "Uxue", "Javier",
            "Iker", "Carlos", "Xabi", "Alejandra", "Carolina", "Iñaki", "Asier", "Maria"]
l = ListaMinusMayus(lista)
print("Lista en minus:", l.a_minus())
print("Lista en mayus:", l.a_mayus())
print("Lista en title:", l.a_title())



# lista[]
# lista=["pedro","xabi","iker"]
# print(lista)

# for usuario in lista:
# print(usuario)

# for pos, usuario in enumerate(lista)
# print(pos,usuario)














