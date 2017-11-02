from ejer02.ejer02 import ListaMinusMayus #rev

lista = ["Beñat", "Xabi", "Xabi", "María", "Alexander", "Carlos", "Juan", "Imanol", "Pedro", "Uxue", "Javier",
            "Iker", "Carlos", "Xabi", "Alejandra", "Carolina", "Iñaki", "Asier", "Maria"]

l = ListaMinusMayus(lista)

num = int(input("Elementos a introducir1: "))
for i in range(num):
    nombre = input("Introduce un nombre: ")
    if l.nombre_posiciones(nombre):
        print("Nombre existente")
    else:
        l.lista.append(nombre.capitalize())
    print(lista)