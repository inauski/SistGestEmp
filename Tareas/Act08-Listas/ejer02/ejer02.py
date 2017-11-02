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

        lm=self.a_minus()
        return lm.count(nombre.lower())

    def nombre_posiciones(self, buscar):
        posic = []
        for i in range(len(self.lista)):
            if self.lista[i].lower() == buscar.lower():
                posic.append(i)
        if len(posic) == 0:
            return False
        else:
            return posic
    def altas_elementos(self):
        print("ALTAS ELEMENTOS - PUEDEN REPETIRSE")
        num = int(input("Elementos a introducir: "))
        for i in range(num):
            nombre = str(input("Introduce un nombre: "))
            lista.append(nombre)
        print(lista)

lista = ["Beñat", "Xabi", "Xabi", "María", "Alexander", "Carlos", "Juan", "Imanol", "Pedro", "Uxue", "Javier",
            "Iker", "Carlos", "Xabi", "Alejandra", "Carolina", "Iñaki", "Asier", "Maria"]
l = ListaMinusMayus(lista)
print("Lista en minus:", l.a_minus())
print("Lista en mayus:", l.a_mayus())
print("Lista en title:", l.a_title())

n=input("Nombre a buscar: ")
print("El nombre aparece",l.cuenta_nombre(n), "veces")

print(l.altas_elementos())

# lista[]
# lista=["pedro","xabi","iker"]
# print(lista)

# for usuario in lista:
# print(usuario)

# for pos, usuario in enumerate(lista)
# print(pos,usuario)