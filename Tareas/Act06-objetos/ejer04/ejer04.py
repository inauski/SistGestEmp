from Factura import Factura


base = float(input("Introduzca base imponible: "))

desc = input("¿ Tienes descuento? s/n ")
if desc  == "s":
    descu = 10
elif desc == "n":
    descu = 0
else:
    print("Debes escribir 's' o 'n' para SI o para NO")
    exit()

iva = input("¿ Dime el IVA a aplicar: General(g) o Reducido(r)? ")
if iva == "g":
    iva = 21
elif iva == "r":
    iva = 6
else:
    print("Introduce 'g' para General o 'r' para reducido")
    exit()

fact = Factura(base,descu,iva)
print("La factura con base imponible {} €".format(base))
print("Tiene {} % de descuento y se queda en {} €".format(descu, fact.base_con_descuento()))
print("Aplicandole un {} % de IVA su valor es de {} €".format(iva,fact.total_iva_incluido()))