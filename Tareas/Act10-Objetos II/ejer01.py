class Agenda(object):
    def __init__(self,lista):
        self.__agenda = lista

    def _getagenda(self):
        return getattr(self,"_Agenda__agenda")
    agenda = property(fget=_getagenda)

    def buscar_en_agenda(self,nombre):
        elem_enc = []
        for elemento in range(len(self.agenda)):
            lista = self.agenda[elemento]
            nomLista = lista[0].title()
            if nomLista == nombre:
                elem_enc.append(lista)
        if len(elem_enc) == 0:
            return False
        else:
            return elem_enc

    def telefonos(self,lis):
        for i in range(len(lis)):
            print(lis[i][1])

def main():
    lista = [("Atanagildo Perez", 694321567), ("Pedro Piqueras", 948123456), ("Alba Gutierrez", 9481356544),
             ("Adela", 9481356588), ("Paco Palancia", 9481356544), ("Berta Piqueras", 9611356544),
             ("Pedro Piqueras", 948222222),
             ("Bertoluchi Contreras", 91381356544), ("Ana", 9476656544), ("Paco Alloz", 9481356544), ("Ana", 947222222)]
    ag = Agenda(lista)
    nom = input("Nombre a buscar: ").title()

    resul = ag.buscar_en_agenda(nom)
    if resul == False:
        print("El contacto no existe")
    else:
        print(nom)
        ag.telefonos(resul)

if __name__ == "__main__":
    main()

