class ListaMinusMayus2:

    def __init__(self,lista):
        self.lista=lista



    def a_mayus(self):
        i=0
        while i < len(self.lista):
            self.lista[i]=self.lista[i].upper()
            i=i+1
        print(self.lista)

    def a_minus(self):
        i = 0
        while i< len(self.lista):

           self.lista[i]=self.lista[i].lower()
           i = i + 1
        print(self.lista)

    def a_title(self):
        i=0
        while i < len(self.lista):
            self.lista[i] = self.lista[i].capitalize()
            i=i+1

        print(self.lista)

    def nombre_posiciones(self):
        nombre = input("introduce un nombre: ")
        i = 0
        a = 0
        while i < len(self.lista):
                if nombre.lower() == self.lista[i].lower():
                    a += 1
                i = i + 1
        print(nombre, " aparece ", a, " veces")

l=ListaMinusMayus2(['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria'])

(l.a_mayus())
(l.a_minus())
(l.a_title())
(l.nombre_posiciones())

