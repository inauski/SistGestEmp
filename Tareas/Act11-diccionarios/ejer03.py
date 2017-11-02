class MaquinaExpendedora(object):

    _total = 0

    def __init__(self):
        self.__productos = {'Palomitas': (1, 10),
                            'Pipas'    : (1, 8),
                            'Doritos'  : (1, 9),
                            'Fanta'    : (1.5, 10),
                            'CocaCola' : (2, 7),
                            'Cafe'     : (0.4, 10),
                            'Aquarius' :(1.5,10)}
        self.__importe = 0
        self.__precio = 0


    def _getimporte(self):
        return getattr(self,"_MaquinaExpendedora__importe")


    def _setimporte(self, importe):
        setattr(self, "_MaquinaExpendedora__importe", importe)


    def _getprecio(self):
        return getattr(self,"_MaquinaExpendedora__precio")

    def _setprecio(self, precio):
        setattr(self,"_MaquinaExpendedora__precio",precio)


    def _getproductos(self):
        return getattr(self, "_MaquinaExpendedora__productos")

    productos = property(fget=_getproductos)
    importe = property(fget=_getimporte, fset=_setimporte)
    precio = property(fget=_getprecio, fset=_setprecio)

    @staticmethod
    def gettotal():
        return getattr(MaquinaExpendedora, "_total")

    @staticmethod
    def settotal(valor):
        setattr(MaquinaExpendedora, "_total", valor)

    def mostrarproduc(self):
        prod = self.productos.keys()
        for p in prod:
            datos = self.productos[p]
            precio = datos[0]
            unidades = datos[1]
            print("{}".format(p))
            print("Precio:{} € Unidades: {}".format(precio,unidades))
        print("")

    def stockproducto(self, nomprod):
        if nomprod in self.productos:
            return True
        else:
            print("No tenemos ese producto")
            return False


    def precioproducto(self, nom_prod):
        return self.productos[nom_prod][0]

    def unidadesproducto(self, nom_prod):
        return self.productos[nom_prod][1]

    def comprobarunidades(self, nom_prod, unid):
        uni = self.unidadesproducto(nom_prod)
        if uni < unid:
            print("Quedan {} unidades de {}.".format(uni,nom_prod))
            return False
        self.restarunidades(nom_prod, unid)
        return True

    def restarunidades(self, nom_prod, unidades):
        precio = self.precioproducto(nom_prod)
        uni = self.unidadesproducto(nom_prod) - unidades
        lis = (precio, uni)
        self.productos.pop(nom_prod)
        self.productos.setdefault(nom_prod, lis)

    def insertar_dinero(self, nom_prod, unidades, importe):
        assert (importe > 0), "Introduzca importe > 0"
        self.importe = self.importe + importe
        self.precio = self.precioproducto(nom_prod) * unidades
        d = self.precio-self.importe
        assert self.precio <= self.importe, ("Le faltan {} euros".format(d))

    def imprimir_ticket(self):
        if self.importe >= self.precio:
            print("Imprimiendo ticket..... Ha introducido {} €".format(self.importe))
            tot = MaquinaExpendedora.gettotal()
            tot = tot + self.precio
            MaquinaExpendedora.settotal(tot)
            self.devolver_cambios()
            return True
        else:
            self.cantidad_pendiente()
            return False


    def devolver_cambios(self):
        print("Que aproveche :) No se olvide de su cambio : {}".format(self.importe-self.precio))
        print()

    def cantidad_pendiente(self):
        print("Introduzca más dinero, le faltan {} euros".format(self.precio-self.importe))

    def vaciar_maquina(self):
        print("Total recaudado por la máquina {}".format(MaquinaExpendedora.gettotal()))
        print("Vaciando máquina...")
        MaquinaExpendedora.settotal(0)
        print("Máquina vaciada {}".format(MaquinaExpendedora.gettotal()))

def main():
    m = MaquinaExpendedora()

    m.mostrarproduc()

    nombre = input("Introduzca nombre del producto a comprar: ").title()

    while True:
        if m.stockproducto(nombre):
            break

    while True:
        try:
            unidades = int(input("¿Cuántas unidades quieres comprar?"))
            assert (unidades > 0), "Debe comprar minimo una unidad del producto"
            if m.comprobarunidades(nombre, unidades):
                break
        except ValueError:
            print("Debe introducir numero")
        except AssertionError as err:
            print(err)

    precio = m.precioproducto(nombre) * unidades
    print("Va ha comprar {} unidadades de {} a {} €".format(unidades,nombre, precio))

    while True:
        try:
            impor = float(input("¿Cuánto dinero mete en la máquina? "))
            m.insertar_dinero(nombre, unidades, impor)
            break
        except ValueError:
            print("Debe introducir numero")
        except AssertionError as err:
            print(err)

    m.imprimir_ticket()
    m.mostrarproduc()
    m.vaciar_maquina()

if __name__ == "__main__":
    main()




