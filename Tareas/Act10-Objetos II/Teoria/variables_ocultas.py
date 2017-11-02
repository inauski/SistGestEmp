# -*- coding: utf8 -*-
MAXIMA_EDAD=35
class Persona():
    _contpersonas=0
    def __init__(self, nombre="sin nombre", edad=0):
        self.nombre = nombre
        # el atritubo _edad no estará visible desde fuera de la clase
        # podremos poner un método con el mismo nombre que el atributo
        self._edad = edad
        Persona._contpersonas+=1

    # método con el mismo nombre que un atributo. En este caso devuelve la edad que interesa, 35 como máximo
    def edad(self):
        return min(self._edad, MAXIMA_EDAD)
    # Las funcionalidades getattr, setattr, delattr y hasattr son complementarias
    # a las funcionalidades propias del objeto.
    def get_edad(self):
        return getattr(self,"_edad")
    def set_edad(self,edad):
        setattr(self, "_edad",edad)
    def del_edad(self):
        delattr(self,"_edad")
    # método estático para acceder a los atributos estáticos
    @staticmethod
    def get_contpersonas():
        return getattr(Persona,"_contpersonas")
    def manejo_edad(self):
        if hasattr(self, "_edad"):
            getattr(self, "_edad")
        else:
            setattr(self, "_edad", 33)

def main():
    p1=Persona("ana",50)
    p2=Persona("paco", 44)


    print ("Atributo _edad ", p1._edad)        #50
    print ("Edad 35 máximo ", p1.edad())       #35

    print ("Edad real: ",p1.get_edad())        #50

    p1.del_edad()                              #borra el atributo _edad
    try:
        print (p1.get_edad())         #intenta escribir la edad pero de error se captura y va a la línea 38
    except:
        p1.manejo_edad()              # no existe _edad y lo crea con 33 años
    print (p1.get_edad())             # 33
    print (p1.edad())
    print ("Total personas: ", Persona.get_contpersonas())

main()
