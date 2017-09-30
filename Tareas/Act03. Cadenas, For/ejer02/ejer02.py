print ("Ejer 2")
frase = str(input("Escribe una frase: "))
print ("En mayusculas: %s" % (frase.upper()) )
print ("En minusculas: %s" % (frase.lower()) )
print ("La letra más alta %s" % max(frase) )
print ("La letra más baja %s" % min(frase) )
let = input("Teclea una letra a-z: ")
let = let.lower()
if frase.lower().__contains__(let):
    print ("%s esta en %s" % (let,frase)) #la 1ª %s hace referencia a let, y la 2ª, a frase, que estan en el parentesis
else:
    print ("%s No esta en %s" % (let,frase))
