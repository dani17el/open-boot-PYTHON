class Juguete:
    _encendido = True

    def __init__(self, x):
        print("Estoy en la clase juguete, en su constructor", x)

    def enciende(self):
        self._encendido = True
        print("Enciendo el aparato")

    def apaga(self):
        self._encendido = False
        print("Apago el aparato")

    def isEncendido(self):
        return self._encendido;

class Dino(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre): # Variable constructor
        super().__init__(nombre)
        print("Estoy en el constructor de la clase Dino()")

    def verEscamas(self):
        pass

_encendido = False
def enciende(nombre):
    print("Invoco a enciende", nombre)


diccionario = {
    'enciende' : enciende,
}

diccionario['enciende']("aaaa")
