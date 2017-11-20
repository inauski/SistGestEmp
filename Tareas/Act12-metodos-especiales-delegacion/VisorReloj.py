import VisorNumero as v1
class VisorReloj(object):
    def __init__(self,hora=None, minuto=None):
        self.__hora = v1.VisorNumero(24)
        self.__minuto = v1.VisorNumero(60)
        if hora != None and minuto != None:
            self.poner_en_hora(hora,minuto)
        else:
            self.poner_en_hora(0,0)

    def _getHora(self):
        return self.__hora
    def _setHora(self,hora):
        self.__hora = hora
    hora = property(fget=_getHora, fset=_setHora)

    def _getMinuto(self):
        return self.__minuto
    def _setMinuto(self,minuto):
        self.__minuto = minuto
    minuto = property(fget=_getMinuto, fset=_setMinuto)

    def poner_en_hora(self,hora,minuto):
        self.hora.valor = hora
        self.minuto.valor = minuto

    def emitir_tic(self):
        self.minuto.incrementar()
        if self.minuto.valor == 0:
            self.hora.incrementar()

    def __str__(self):
        return str("%s:%s" % (self.hora,self.minuto))


def emulador(reloj):
    cont = 0
    while True:
        cont += 1
        print(reloj,end=" ")
        if cont > 10:
            print()
            cont = 0
        reloj.emitir_tic()
        if(reloj.hora.valor == 0 and reloj.minuto.valor == 0):
            break


def main():
    v = VisorReloj()
    print("Hora 1: {}".format(v))
    v.emitir_tic()
    print("Hora 1 + 1 minuto: {}".format(v))

    v2 = VisorReloj(23,00)
    print("Hora 2: {}".format(v2))
    v2.emitir_tic()
    print("Hora 2 + 1 minuto: {}".format(v2))

    v3 = VisorReloj(12,59)
    print("Hora 3: {}".format(v3))
    v3.emitir_tic()
    print("Hora 3 + 1 minuto: {}".format(v3))

    v4 = VisorReloj(23,59)
    print("Hora 4: {}".format(v4))
    v4.emitir_tic()
    print("Hora4 + 1 minuto: {}".format(v4))



if __name__== "__main__":
    main()