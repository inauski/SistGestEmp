class Agenda(object):
    def __init__(self,agenda):
        self.__agenda= agenda

    def _getagenda(self):
        return getattr(self,"_Agenda__agenda")
    agenda=property(fget=_getagenda)

    def buscar_agenda(self,nombre_buscar):
        if nombre_buscar in self.agenda:
            return self.agenda[nombre_buscar]
        else:
            return False
        #return self.agenda.get(nombre_buscar)

    @staticmethod
    def telefono_correcto(tel):
        assert (len(tel) == 9 and tel.isdigit()), "Error telefono"
        return True

            #assert(tel.isdigit()), "Introduce numero"

    def anadir_telefono(self,nombre,telefono):
        #self.agenda(telefono)
       self.agenda[nombre]=telefono
    def escribir(self):
        print(self.agenda)

def main():
    lista = {'Adela': '444444444', 'Pedro': '222222222', 'Bertoluchi': '777777777', 'Paco': '555555555', 'Berta': '666666666', 'Alba': '333333333', 'Ana': '111111111'}

    ag=Agenda(lista)
    nombre = input("Nombre a buscar: ").title()

    if ag.buscar_agenda(nombre) == False:
        try:
            tel = input("Introduce numero de telefono: ")
            ag.telefono_correcto(tel)
            ag.anadir_telefono(nombre,tel)
            print("Añadido")
        except AssertionError as err:
            print(err)
    else:
        try:
            tele = ag.buscar_agenda(nombre)
            tel = input("{} Modificar {} (Enter:no modificar:) ".format(nombre,tele))
            ag.telefono_correcto(tel)
            ag.anadir_telefono(nombre,tel)
            print("Actualizado")
        except AssertionError as err:
            print(err)
    ag.escribir()

if __name__ == "__main__":
    main()


