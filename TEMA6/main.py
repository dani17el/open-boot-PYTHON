class Juguete:
    _encendido = True

    def enciende(self):
        self._encendido = True
        print("Enciendo el aparato")

    def apaga(self):
        self._encendido = False
        print("Apago el aparato")

    def isEncendido(self):
        return self._encendido;

class Potato(Juguete):
    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass

class Dino(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre): # Variable constructor
        self.color = "Verde"
        self.nombre = nombre

    def __del__(self):  # variable destructor
        print("Estoy en el destructor de la clase", self.__class__)

    def verEscamas(self):
        pass

p = Dino("midinosaurio")
print("a")
print("b")
p.verEscamas()
del (p) #Esta es la funcion que invoca al destructor de variable

