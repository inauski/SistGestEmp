class Fusion:
    def __init__(self,listaUno,listaDos):
        self.listaUno=listaUno
        self.listaDos=listaDos
    def fusionar(self):
        nuevaLista = []
        for i in range(len(self.listaUno)):
            nuevaLista.append([self.listaUno[i],self.listaDos[i]])
        return nuevaLista

nombres = ["iñaki","ion","paco","julen"]
correo=["isan@gmail.com","ion@gmail.com","paco@hotmail.com","julen@jul.com"]

l = Fusion(nombres,correo)
print(l.fusionar())


