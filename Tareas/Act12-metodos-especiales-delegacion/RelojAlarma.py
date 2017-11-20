import VisorReloj as v
import Alarma as a

class RelojAlarma(object):
    def __init__(self,visor_reloj, alarma):
        self.visor_reloj = visor_reloj
        self.alarma = alarma

    def gethora(self):
        return self.visor_reloj

    def setalarma(self,hora,minuto):
        self.alarma._setalarma(hora,minuto)

    def _es_hora_alarma(self):
        return str(self.visor_reloj) == str(self.alarma)

    def getalarma(self):
        return self.alarma

    def emitir_tic(self):
        self.visor_reloj.emitir_tic()
        if self._es_hora_alarma():
            print("Riiiiinnnnngggg")



def main():
    hora1 = v.VisorReloj(18, 33)
    alarma1 = a.Alarma(18, 35)
    mirel = RelojAlarma(hora1, alarma1)

    for i in range(5):
        mirel.emitir_tic()
        print(mirel.gethora())

    mirel.setalarma(18,40)

    for i in range(5):
        mirel.emitir_tic()
        print(mirel.gethora())

if __name__== "__main__":
    main()
