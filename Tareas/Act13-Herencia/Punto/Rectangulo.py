import Punto
class Rectangulo(Punto):

    def __init__(self,base,altura,x,y):
        self.base = base
        self.altura = altura
        self.x = x
        self.y = y

    def __str__(self):
        return ("Base: %d, Altura: %d" % self.base , self.altura)

    def centro_rectangulo(self):
        return ("%d, %d") % ((self.x + self.base)/2, (self.y + self.base)/2)

    def agrandar_rectangulo(self,masbase,masaltura):
        self.base += masbase
        self.altura += masaltura

    def mover_rectangulo(self,Punto):
        pass

