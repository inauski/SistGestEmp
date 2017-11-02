class Contactos(object):

    def __init__(self,lista):
        self.__agenda=lista
    def _getagenda(self):
        return getattr(self,"_Contactos__agenda")
    agenda=property(fget=_getagenda)

    def contactos_unificados(self):
        dic_aux={}
        for i in range(len(self.agenda)):
            lisAux = []
            nom = self.agenda[i][0]
            tel = self.agenda[i]

            for j in range(1,len(tel)):
                lisAux.append(tel[j])
            if nom in dic_aux:
                lista = []
                lista = dic_aux.get(nom)
                total = lista + lisAux
                #Devuelve el valor que corresponde con la clave y luego borra la clave y el valor
                dic_aux.pop(nom)
                dic_aux.setdefault(nom,total)
                #Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta

            else:
                dic_aux.setdefault(nom,lisAux)
        return dic_aux


def main():
    lista= [('Ana', 'correo1@ana.es', 'correo2@ana.es'), ('Maria', 'correo1@maria.es'), ('Iker', 'correo1@iker.es'), ('Ana', 'correo3@ana.es', 'correo4@ana.es'), ('Iker', "correo'2@iker.es"), ('Ana', 'correo5@ana.es')]

    c = Contactos(lista)

    dic = c.contactos_unificados()
    for i in dic:
        print (i,dic.get(i))

if __name__ == "__main__":
    main()
