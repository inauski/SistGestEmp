print ("Convertidor de pies y pulgadas a centímetros")
pies = float(input("Escriba una cantidad de pies: "))
pulgadas = float(input("Escriba una cantidad de pulgadas: "))
print(str(pies) + " pies " + str(pulgadas) + " pulgadas son " +  str((pies*12 + pulgadas) * 2.54) + " cm")
