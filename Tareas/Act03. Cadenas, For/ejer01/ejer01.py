print ("Recorrer cadena")
frase = str(input("Escribe una frase: "))
for i in frase:
    print (i)
pos = int(input("Teclea posición 1-%s: " % len(frase)))
print ("Desce el Inicio: posición %s carácter %s" % (pos,frase[pos-1:pos]))
print ("Desce el Final: posición %s carácter %s" % (pos,frase[len(frase)-pos:len(frase)-pos+1]))
print ("Los primeros %s caracteres: %s" % (pos,frase[:pos]))
print ("Los ultimos %s caracteres: %s" % (pos,frase[-pos:]))

