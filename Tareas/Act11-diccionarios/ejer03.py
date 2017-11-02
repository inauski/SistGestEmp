class MaquinaExpendedora(object):

    _total = 0
    def __init__(self,producto,precio):
        self.__precio = precio
        self.producto=producto
        self.__cantidad=0

    def _getimporte(self):
        return getattr(self, "_MaquinaExpendedora__importe")
    def _setimporte(self,importe):
        setattr(self,"_MaquinaExpendedora__importe", importe)

    def _getprecio(self):
        return getattr(self, "_MaquinaExpendedora__precio")
    def _setprecio(self,precio):
        setattr(self, "_MaquinaExpendedora__precio",precio)

    @staticmethod
    def getTotal():
        return getattr(MaquinaExpendedora, "_total")
    def setTotal(valor):
        setattr(MaquinaExpendedora, "_total", valor)

    precio = property(fget=_getprecio, fset=_setprecio)
    importe = property(fget=_getimporte, fset=_setimporte)

    def comprarproducto(self):
        if self.producto == "apagar":
            self.apagar()
        else:
            pass
    def getcantidad(self):
        return self.__cantidad

    def apagar(self):
        if (self.producto == 0):
            self.precio=0
            self.__cantidad=0


    def insertar_dinero(self, cantidad):
            # Este assert y el siguiente se controlan en el tercer while del main
            assert (cantidad > 0), "Introduzca cantidad positiva"
            self.importe = self.importe + cantidad
            dev = self.precio - self.importe
            assert self.precio <= self.importe, ("Dinero insuficiente, le faltan {}".format(dev))

    def imprimir_ticket(self):
            if self.importe >= self.precio:
                print("Imprimiendo ticket .... Ha introducido {}".format(self.importe))
                tot = self.getTotal()
                tot = tot + self.precio
                MaquinaExpendedora.setTotal(tot)

                # Devolver los cambios
                self.devolver_cambios()
                # ponemos _importe a 0 para que no acumule el dinero metido desde el principio
                self.__importe = 0
                return True

            else:
                self.cantidad_pendiente()
                return False

        def devolver_cambios(self):
            print("Que aproveche :) No se olvide de su cambio: {}".format(self.importe - self.precio))

        def cantidad_pendiente(self):
            print("No ha introducido dinero suficiente, le faltan {}".format(self.precio - self.importe))

        def vaciar_maquina(self):
            print("Total recaudado por la máquina {}".format(self.getTotal()))
            print("Vaciando máquina...")

            # Ponemos a 0 la maquina
            MaquinaExpendedora.setTotal(0)
            print("Máquina vaciada {}".format(MaquinaExpendedora.getTotal()))

def main():
    m = MaquinaExpendedora(0,0)

    while True:
        try:
            produc = int(input("¿Qué producto quiere?"))
            assert (produc > 0), "Los productos pedidos tienen que ser >= 0"
            break
        except ValueError:
            print("Debe introducidor numero")
        except AssertionError as err:
            print(err)
    for i in range(1, produc + 1):
        while True:
            try:
                precio = float(input("Cafe {}. Teclee su precio: ".format(i)))
                assert (precio > 0), "Introduzca cantidad positiva"
                print("Supongo que quiere 1 producto y cuesta {}".format(float(precio)))
                m.precio = precio
                break
                # en caso de otra cosa q no sea numero
            except ValueError:
                print("Debe introducir numero")
                # si el precio es menor que 0
            except AssertionError as err:
                print(err)

        while True:
            try:
                cant = float(input("¿Cuanto dinero mete en la máquina? "))
                m.insertar_dinero(cant)
                break
            # en caso de otra cosa q no sea numero
            except ValueError:
                print("Debe introducir número")
            # en caso de que falte dinero por introducir o sea numero negativo (assert lineas 26 y 30)
            except AssertionError as err:
                print(err)
        # imprimimos el ticket con la instancia creada m llamando al metodo imprimir_ticket
        m.imprimir_ticket()
        # vaciamos la maquina con la instancia creada m llamando al metodo vaciar_maquina
    m.vaciar_maquina()

if __name__ == "__main__":
        main()









