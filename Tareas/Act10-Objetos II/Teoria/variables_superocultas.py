# -*- coding: utf8 -*-
class AtributosEscondidos():
    __suma=0
    def __init__(self,nom,edad):
        self.__nombre=nom
        self.__edad=edad
        AtributosEscondidos.__suma+=1
    def setedad(self,edad):
        setattr(self,"__edad",edad)
    def getedad(self,edad):
        getattr(self,"__edad")
def main():
    a=AtributosEscondidos("Pepe",45)
    print (a._AtributosEscondidos__nombre)
    print (a._AtributosEscondidos__edad)
    # sum=AtributosEscondidos.__suma

main()
