print ("Ejer 4")
frase = input("Escribe un correo: ")
if frase.__contains__("gmail.com"):
    print ("Termina en gmail.com")
else:
    print ("No termina en gmail.com")
print ("Cantidad de '@': %s" % frase.count('@'))
print ("@ esta en: %s" % (frase.index('@')))
print ("Usuario: %s" % (frase.split("@")[0]))
print ("Dominio: %s" % (frase.split("@")[1]))
