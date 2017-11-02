list = [3, 1, 9, 8, 6]
print(sorted(list)) #[1, 3, 6, 8, 9] Menor a mayor

print(sorted(list, reverse = True)) #[9, 8, 6, 3, 1] Mayor a menor

print(list) #[3, 1, 9, 8, 6] Lista original

listaLetras = ["be", "ab", "cc", "aa", "cb"]
listaLetras.sort()
print(listaLetras) #["aa", "ab", "be", "cb", "cc"]

listaNum = (1,2,3,4,5)
for indice, valor in enumerate(listaNum): #Si queremos que nos devuelva el indice utilizamos enumerate
    print(valor, "tiene el indice", indice)

#Si en un futuro la lista crece, es mejor poner
for valor in range(0, len(listaNum)): #empieza a contar el 0 y termina en la longitud de la lista, por lo tanto, no hace falta saber el tope
    print(valor)

diccionario = {'clave1': 10, 'clave2':20, 'clave3':500 } #clave:valor
for clave, valor in diccionario.items():#se puede poner .keys o .values
    print("La clave", clave, "tiene el valor de ",valor)