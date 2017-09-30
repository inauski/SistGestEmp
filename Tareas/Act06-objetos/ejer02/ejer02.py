import re

class CocheITV:
    def __init__(self, matricula,anio):
        self.matricula = str(matricula)
        formato = re.compile("[0-9]{4}-[A-Za-z]{3}")
        self.anio = anio
        if formato.match(matricula) is None:
            print("Error, has introducido mal la matricula")
            exit()

    def siguienteitv(self):
        return self.anio + 4

    def toString(self):
        print("El coche con matricula {} del año {}, pasara la siguiente itv en el año {}".format(self.matricula, self.anio, self.siguienteitv()))

#PRUEBA 1
p1 = CocheITV("1234-aaa",2012)
print("Matricula ", p1.matricula)
print("Año: ", p1.anio)
print("El coche ", p1.matricula, " tiene que volver a pasar la ITV en ", p1.siguienteitv())

#PRUEBA 2 con input

mat = input("Inserte una matricula: ")
anno = int(input("Inserte un año: "))
coche = CocheITV(mat, anno)
coche.toString()




