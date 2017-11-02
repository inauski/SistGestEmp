class CreaUsuario:#rev

    def __init__(self,nombrecompleto):
        self.nombrecompleto=nombrecompleto

    def usuario(self):
        print(self.nombrecompleto)
        usuario=""
        usuario+=self.nombrecompleto[0][0:1]
        usuario+=self.nombrecompleto[1][0][0:6]
        usuario+=self.nombrecompleto[1][1][0:3]
        return usuario

usu = []
nombres_apellidos = [['Pedro', ['Rodriguez', 'Saavedra']], ['Iker', ['Fernandez', 'Ochoa']],
                         ['Carlos', ['Izu', 'Rodriguez']], ['Paco', ['Rodriguez', 'Ochoa']]]
for usuario in nombres_apellidos:
    creado = CreaUsuario(usuario)
    usu.append(creado.usuario())
    print("Lista de usuarios: ",usu)

#Ej sin usar clase
    # for pos, nom in enumerate(nombres_apellidos):
    # #inicial nombre
    #     usu = nom[0][0]
    # #primer apellido
    #     ape = len(nom[1][0])
    #     if ape < 7:
    #         usu = usu + nom[1][0]
    #         if len(usu) < 8:
    #             ape = len(usu)
    #             f = 8 - ape
    #             usu = usu + nom[1][1][0:f]
    #     elif ape > 7:
    #         usu = usu + nom[1][0][0:6]
    #     usuarios.append(usu.lower())
    # print("Lista de nombres: %s" % nombres_apellidos)
    # print("Lista usuarios: %s" % usuarios)
    #
