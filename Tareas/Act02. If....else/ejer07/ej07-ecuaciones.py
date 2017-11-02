print("Ecuacion 'a x + b = 0'")
a = float( input("Escriba coeficiente 'a': ") )
b = float( input("Escriba coeficiente 'b': ") )
if a == 0:
    if b == 0:
        print("Todos los números son solución")
    else:
        print("No hay solución")
else:
    print("La solución es: %0.1f" % (-b/a))

