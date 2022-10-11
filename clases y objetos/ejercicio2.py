class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 51:
            print("El estudiante", self.nombre, "con una nota de", self.nota, "queda aprobado")
        else:
            print("El estudiante", self.nombre, "con una nota de", self.nota, "queda reprobado")


alumno1 = Alumno("Freddy", 80)
alumno1.aprobado()
alumno2 = Alumno("Carlos", 45)
alumno2.aprobado()
