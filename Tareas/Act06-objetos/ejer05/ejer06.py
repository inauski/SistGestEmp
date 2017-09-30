class Alumno:
    'Clase para alumnos'
    numalumnos = 0 #comunes al objeto alumno
    sumanotas = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        Alumno.numalumnos += 1
        Alumno.sumanotas += nota

    def mostrarNombreNota(self):
        return(self.nombre, self.nota)

    def mostrarNumAlumnos(self):
        return(Alumno.numalumnos)

    def mostrarSumaNotas(self):
        return(Alumno.sumanotas)

    def mostrarNotaMedia(self):
        if Alumno.numalumnos > 0:
            return(Alumno.sumanotas/Alumno.numalumnos)
        else:
            return("Sin alumnos")

        #En este ejemplo se utilizan variables de clase que no habíamos utilizado en los anteriores

        #alumno1 = Alumno("Maria", 8)
        #alumno2 = Alumno("Carlos", 6)
        #Después crea objetos de la clase como los dos ejemplos de arriba