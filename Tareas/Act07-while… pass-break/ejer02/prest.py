class Prestamo (object):
    cuenta_prestamos = 0
    acumula_prestamos = 0
    acumula_intereses = 0

    def __init__(self,capital, tipointeres, anios):
        self.capital = capital
        self.tipointeres = tipointeres
        self.anios = anios
    def calcularinteres(self):
        return self.capital*self.tipointeres*self.anios/100







