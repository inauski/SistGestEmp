class Grados: #REV

    def __init__(self,centigrados, farenheit):
        self.centigrados = centigrados
        self.farenheit = farenheit
    def acentigrados(self):
        return ((self.farenheit -32)*5) / 9
    def afarenheit(self):
        return (self.centigrados *9 /5) + 32

cont_temp = 0
grados10 = 10

while True:
    if cont_temp == 12:
            break
    grad = Grados(0,grados10)
    print("{} F = {:.5} C".format(grados10,grad.acentigrados())) #{:.5} es para decirle cuantos num queremos imprimir
    grados10 += 10
    cont_temp += 1
print("Total de temperaturas convertidas:" , cont_temp)




