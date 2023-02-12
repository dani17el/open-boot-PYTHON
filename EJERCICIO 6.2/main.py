class Alumno:
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno aprobó")

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.datos("Dani", 8)
alumno2.datos("Fatima", 4)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
