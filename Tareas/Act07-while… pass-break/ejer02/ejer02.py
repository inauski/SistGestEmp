import prest

def main():
    while True:
        cap = int(input("Capital (0=Salir) "))
        if (cap == 0):
            break
        inter = int(input("Tipo de interés % "))
        ano = int(input("Años: "))

        prest.Prestamo.cuenta_prestamos += 1
        prest.Prestamo.acumula_prestamos += cap


        prestamo= prest.Prestamo(cap, inter, ano)
        print("Total interes: ", prestamo.calcularinteres())
        prest.Prestamo.acumula_intereses = prestamo.calcularinteres()



    print("Total de préstamos: ", prest.Prestamo.cuenta_prestamos)
    print("Capital prestado: ",  prest.Prestamo.acumula_prestamos)
    print("Total de intereses: ",prest.Prestamo.acumula_intereses )

if __name__ == '__main__':
    main()




