"""
Ejemplo de funcion
"""
def factorial_numero(numero): #pasandole el argumento 'numero' podemos hacer el factorial para el num q queramos

    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial #si ponemos return, estamos OBLIGADOS a CREAR una VARIABLE despues para printar el resultado, si nos sale NONE(vacio) como resultado es pq falta el RETURN
resul = factorial_numero(4) #escribimos solo el nombre de la funcion las veces q queramos, en vez de otra vez todo el codigo
print(resul)
#factorial_numero(5)

"""
Ejemplo de funcion(II)
"""
def suma(valor_uno,valor_dos,valor_tres):
    return valor_uno + valor_dos + valor_tres
resul = suma(10,20,30)
print(resul)

def division(valor_uno,valor_dos):
    return valor_uno / valor_dos
resul = division(100,10) #100 corresponde a valor_uno y 10 a valor_dos, pero si los ponemos asi ->resul = division(10,100) seria al reves y no da el mismo resultado
print(resul)

def multiplicacion(valor_uno,valor_dos = 10): #podemos asignarle un valor por defecto, ahora, si luego abajo le damos otro valor prevalecera antes que este
    return valor_uno * valor_dos
resul = multiplicacion(2,3)
print(resul)

def multiples_valores(): #
    return "String", True, 2.0
resul = multiples_valores()
#print(resul) #devuelve una tupla ('String', True, 2.0) por lo tanto, podemos printar por posicion.
string = resul[0] #en el indice 0 tenemos un string
boleano = resul[1] #en el indice 1 tenemos un boolean, etc.
flo = resul[2]
#otra forma mas corta de escribir lo mismo es: string, boleano, flo = multiples_valores() ,que nos devolvera el string para indice 0, True para 1 ,etc, pero tiene q haber las mismas variables que haya en el return
print(string,boleano,flo)

"""
Una funcion dentro de otra funcion
"""

mi_variable = multiplicacion #creamos una variable con la funcion 'multiplicacion'
def mostrar_resultado(funcion): #recibe una funcion , la ejecuta y la printa
    print(funcion(4,6))
mostrar_resultado(mi_variable) #le pasamos la variable creada

"""
Ejemplo de factorial para UN solo numero,el 5

def factorial_numero():
    numero = 5
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
factorial_numero()
"""
