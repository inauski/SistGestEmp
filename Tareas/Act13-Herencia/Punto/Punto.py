class Punto(object):
    def __init__(self,x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self,x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self,y):
        self.__y = y

    x = property(fget=getX,fset=setX)
    y = property(fget=getY,fset=setY)

    def __str__(self):
        return  "%d , %d"  % (self.__x, self.__y)

    def __eq__(self, other):
        if self.__str__() == other:
            return True

    def metodo(self):
        print("Ejecutando la clase padre")



