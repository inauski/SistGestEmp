class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def area_cuadrado(self):
        return self.lado * self.lado

class Rectangulo:

    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
    def area_rectangulo(self):
        return self.base * self.altura

def menu(self):
    print("Calculo de áreas")
    print("1.Cuadrado")
    print("2.Rectangulo")

opc = int(input("Teclea una opcion (1-2): "))
if (opc == 1):
        lad = int(input("Lado del cuadrado:" ))
        lad = Cuadrado(lad)
        print("El área del cuadrado es: ", lad.area_cuadrado())
if (opc == 2):
        bas = int(input("Base: "))
        alt = int (input("Altura:"))
        area = Rectangulo(bas,alt)
        print ("El área del rectangulo es", area.area_rectangulo())



