from ejer02 import ListaMinusMayus
lista = ["Beñat", "Xabi", "Xabi", "María", "Alexander", "Carlos", "Juan", "Imanol", "Pedro", "Uxue", "Javier",
            "Iker", "Carlos", "Xabi", "Alejandra", "Carolina", "Iñaki", "Asier", "Maria"]

l = ListaMinusMayus(lista)

l.modificaciones(input("Nombre a buscar: "))
print(lista)

