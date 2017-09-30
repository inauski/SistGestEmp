print ("Ejer 3")
frase = input("Escribe una frase: ")
if frase.isalnum():
    print ("%s es alfanumérica, números y letras" % frase)
if frase.isalpha():
    print ("%s es alfabética" % frase)
if frase.isdigit():
    print ("%d es un número" % float(frase))
if frase.islower():
    print ("%s es minúscula" % frase)
if frase.isspace():
    print ("%s es un espacio" % frase)
if frase.istitle():
    print ("%s tiene formato de titulo" % frase)
if frase.isupper():
    print ("%s es mayuscula" % frase )
