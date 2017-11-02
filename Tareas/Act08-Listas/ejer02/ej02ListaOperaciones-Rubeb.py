import ej01ListaNombres as listaNombres

class listaMinusMayus:
    lista = []
    def __init__(self,lista):
        self.lista = lista
    def a_mayus(self):
        listAux = []
        for s in self.lista:
            listAux.append(s.upper())
        self.lista = listAux
    def a_minus(self):
        listAux = []
        for s in self.lista:
            listAux.append(s.lower())
        self.lista = listAux
    def a_title(self):
        listAux = []
        for s in self.lista:
            listAux.append(s.title())
        self.lista = listAux
    def cuenta_nombre(self,nombre):
        self.a_minus()
        return self.lista.count(nombre.lower())
    #Complemento añadido por el ejercicio 4
    def nombre_posiciones(self,nombre):
        pos = []
        self.a_title()
        nombre = nombre.title()
        if not nombre in self.lista:
            return False
        else:
            for i in range(len(self.lista)):
                if self.lista[i] == nombre:
                    pos.append(i)
            return pos
    def buscaYReemplaza(self,nombre):
        auxListaMM = listaMinusMayus(self.lista)
        auxListaMM.a_minus()
        try:
            pos = auxListaMM.lista.index(nombre.lower())
            nuevoNombre = input("NUEVO nombre: ")
            print("Se ha remplazado ", nombre, " por ", nuevoNombre)
            self.lista[pos] = nuevoNombre
        except ValueError as e:
            print(nombre, " no está en la lista")

def main():
    lista = listaNombres.pedirLista()
    lstMinMay = listaMinusMayus(lista)
    print("La lista original es: ",lista)
    lstMinMay.a_mayus()
    print("La lista en mayúsculas es: ",lstMinMay.lista)
    lstMinMay.a_minus()
    print("La lista en mayúsculas es: ",lstMinMay.lista)
    lstMinMay.a_title()
    print("La lista en mayúsculas es: ",lstMinMay.lista)
    nombre = input("Nombre a buscar:")
    print(nombre.title(), " aparece ",lstMinMay.cuenta_nombre(nombre), " veces.")

if __name__ == "__main__":
    main()