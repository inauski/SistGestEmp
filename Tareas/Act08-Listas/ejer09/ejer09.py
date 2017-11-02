class NombrePersona: #MAL
    nom=""
    apellido=""

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def iniciales(self):
        nom = self.nombre.split(" ")
        iniciales = ""

        for i in nom:
            iniciales += i[0].upper() + ". "


        print("Nombre: ",self.nombre)
        print("Apellido: ", self.apellido)
        print("Iniciales: ", iniciales)
        print(iniciales,  self.apellido)
        print(self.apellido ,self.nombre)
l = NombrePersona("Pedro Jose", "del amor hermoso")
l.iniciales()

#metodo strip para quitar espacios en blanco,caracteres...