"""
Esto es lo mismo que lo de abajo pero en más lineas de codigo
lista = [] #False
for valor in range(0,11)
    lista,append(valor)
"""
lista = [valor for valor in range(0,11) ] #El primer 'valor' es el que hace posible que se agreguen valores a la lista, lo mismo que append.
#tb posible esto lista = [ valor for valor in range(0,11) if valor % 2 == 0 ] q devuelve los pares
print(lista)

tupla = tuple(valor for valor in range(0,11) if valor % 2 != 0 ) #impares, con la parte condicional if valor % 2 != 0
print (tupla)

diccionario = {clave:valor for clave, valor in enumerate(lista) }#enumerate devuelve clave y valor, se puede poner por ej la condicional if clave < 5 y solo imprime las claves de 0 a 4
print(diccionario)