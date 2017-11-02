class Contactos(object):

    def __init__(self,lista):
        self.__agenda=lista
    def _getagenda(self):
        return getattr(self,"_Contactos__agenda")
    agenda=property(fget=_getagenda)

    def contactos_unificados(self):

        dic_aux={}
        for i in range(len(self.agenda)):
            lis = []
            nom = self.agenda[i][0]
            tel = self.agenda[i]

            for j in range(1,len(tel)):
                lis.append(tel[j])
            if nom in dic_aux:
                li = []
                l = dic_aux
                
        return dic_aux


def main():
    lista= [('Ana', 'correo1@ana.es', 'correo2@ana.es'), ('Maria', 'correo1@maria.es'), ('Iker', 'correo1@iker.es'), ('Ana', 'correo3@ana.es', 'correo4@ana.es'), ('Iker', "correo'2@iker.es"), ('Ana', 'correo5@ana.es')]

    c = Contactos(lista)

    dic = c.contactos_unificados()
    for i in dic:
        print(dic.get(i))

if __name__ == "__main__":
    main()
