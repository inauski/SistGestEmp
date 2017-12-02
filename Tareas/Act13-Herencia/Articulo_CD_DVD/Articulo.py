# import gi
# from gi.repository import Gtk

class Articulo():
    def __init__(self,tipo, titulo,duracion,lotengo=False,comentario=""):
        self.tipo = tipo
        self.titulo = titulo
        self.duracion = duracion
        self.lotengo = lotengo
        self.comentario = comentario

    def __str__(self):
        return  "{},{},{},{},{} ".format(self.tipo,self.titulo,self.duracion,self.lotengo,self.comentario)

# a = Articulo("CD","Hola",30,True,"aaa")
# print(a)

class BaseDeDatos():
    def __init__(self,lista,articulos=None):
        self.__lista_articulos = lista


    def _getArticulos(self):
        return self.articulos

    def _setArticulos(self,valor):
        self.articulos = valor

    lista_articulos = property(fget=_getArticulos,fset=_setArticulos)

    def consultar(self,titulo):
        if not self.titulo is None:
            return self.articulos
        else:
            return "No esta"

    def escribir_articulos(self):
        self.Articulo.__str__()

    def get_articulo(self,i):
        if True:
            for i in self.articulos:
                return self.articulos[i]
        else:
            print("Error")

    def set_articulo(self,articulo):
        dic_aux = {}
        for i in range(len(self.articulos)):
            lista = []
            a = self.articulos(i)
            for j in range (1,len(a)):
                lista.append(articulo[j])

class CD(Articulo.Articulo):
    def __init__(self):
        super(CD, self).__init__(artista,pistas)
        self.artista = artista
        self.pistas = pistas


    def __str__(self):
        return
def crear_bbdd(bbdd):
    pass


class DVD(Articulo.Articulo):
    def __init__(self):
        super(DVD,self).__init__(director)
        self.director = director




