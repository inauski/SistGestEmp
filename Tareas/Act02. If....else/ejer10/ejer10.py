print("CONVERTIDOR DE CM A KM, M Y CM")
centimetros = int(input("Escriba una distancia en centímetros: "))

kilometros = centimetros // 100000
metros = centimetros % 100000 // 100
resto = centimetros % 100

print(str(centimetros) +  " cm son " +str(kilometros) + " km " + str(metros) + " m y "+ str(resto) +  " cm")