# -*- coding: utf8 -*-
"""Esta función nos permite crear propiedades con nombre que pueden reemplazar a los atributos. Las propiedades se acceden
     igual que los atributos, pero detrás de las escenas se llaman a los métodos que especificamos para obtener y
     establecer el valor."""
class Rectangle(object):
    def __init__(self, width, height):
        #variable privado u oculta con dos guiones bajos.
        self.__width = width
        self.height = height
    # ocultamos el método con el mismo nombre que la que va a ser la propiedad
    def _getwidth(self):
        return self.__width
    def _setWidth(self, width):
        self.__width = width
    width = property(fget=_getwidth, fset=_setWidth)

    def getHeight(self):
        return self.height
    def setHeight(self, height):
        self.height = height

    def _area(self):
        # return self.getWidth() * self.getHeight()
        return self.width * self.getHeight()
    area = property(fget=_area)
"""La función property () de Python puede usarse para especificar un getter, un setter, un deletion
, y una docstring. Dado que sólo especificamos un getter, la propiedad del área es
solo lectura. Si más adelante necesitamos realizar algún cálculo cuando el ancho
se accedió, podríamos simplemente convertirlo en una propiedad, así:"""

def main():
    rectangul1=Rectangle(2,4)
    print (rectangul1.area)
    rectangul1.width=5
    print(rectangul1.area)
main()