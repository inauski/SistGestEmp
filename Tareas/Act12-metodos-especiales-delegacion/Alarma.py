
class Alarma(object):
    def __init__(self,hora=None,minutos=None):
        self.__hora=hora
        self.__minutos=minutos

    def _getHora(self):
        return self.__hora
    def _setHora(self, hora):
        self.__hora = hora
    hora = property(fget=_getHora, fset=_setHora)

    def _getminutos(self):
        return self.__minutos
    def _setminutos(self,valor):
        self.__minutos=valor
    minutos= property(fget=_getminutos,fset=_setminutos)

    def _getalarma(self):
        return self.__str__()

    def __str__(self):
        return "%.2d:%.2d" % (self.hora, self.minutos)

    def _setalarma(self,hora,minutos):
        self.__hora=hora
        self.__minutos=minutos

# a = Alarma()
# print(a)


