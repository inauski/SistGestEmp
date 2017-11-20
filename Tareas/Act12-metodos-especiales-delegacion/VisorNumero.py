class VisorNumero(object):

    def __init__(self,limitemaximo):
        self.__valor = 0
        self.__limite = limitemaximo

    def _getlimite(self):
        return self.__limite
        # return getattr(self,"_VisorNumero__limite")
    def _setlimite(self,limite_maximo):
        self.__limite = limite_maximo
        # setattr(self, "_VisorNumero__limite_maximo", limite_maximo)
    limite=property(fget=_getlimite,fset=_setlimite)

    def _getvalor(self):
        return self.__valor
        # return getattr(self,"_VisorNumero__valor")
    def _setvalor(self,nuevo_valor):
        self.__valor=nuevo_valor
    valor=property(fget=_getvalor,fset=_setvalor)

    def __str__(self):
        return "%.2d" % self.valor

        # msg = str(self.valor).zfill(2)  # zfill rellena la cadena a la izquierda con ceros
        # return "{}".format(msg)

    def incrementar(self):
        self.valor=(self.valor+1) % self.limite

        # self.valor += 1
        # if self.valor == self.limite:
        #      self.valor = 0


def main():

    hora = VisorNumero(24)
    minuto = VisorNumero(60)

    print("Hora: ")
    for i in range(90):
        hora.incrementar()
        print(hora, end="-")

    print("\n")

    print("Minuto: ", )
    for i in range(90):
        minuto.incrementar()
        print(minuto, end="-")

if __name__ == "__main__":
        main()

