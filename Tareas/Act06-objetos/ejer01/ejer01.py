class Prestamo:
    def __init__(self, capital,tipointeres,anios):
        self.capital = capital
        self.tipointeres = tipointeres
        self.anios = anios
    def calcularinteres(self):
        return self.capital*self.tipointeres*self.anios/100

p1 = Prestamo(12000,5,30)

print("\nPRESTAMO 1")
print ("Capital: " , p1.capital)
print("Tipo interes: ", p1.tipointeres, "%")
print("Años:", p1.anios)
print("Total intereses:", p1.calcularinteres())

try:
    cap = int(input("Dime un capital: "))
    inter = int(input("Dime un interes: "))
    ano = int(input("Dime los años: "))



    print ("PRESTAMO 2")
    print ("Capital: ", cap)
    print("Tipo interes:", inter , "%")
    print("Años: ", ano)
    totinter = Prestamo(cap,inter,ano)
    print("Total interes: ",totinter.calcularinteres())
except ValueError as e:
    #ERROR
   print(e)


