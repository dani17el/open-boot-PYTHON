
class Color:
    colorCoche = "Rojo"

class Ruedas:
    ruedasCoche = 4

class Puertas:
    puertasCoche = 5


class Coche:
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()

class Vehiculo(Coche):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = Color
        self.ruedas = Ruedas
        self.puertas = Puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return"color{},ruedas {}, puertas{}, km/h {}, cc{}".format(self.color, self.ruedas, self.puertas,
                                                                   self.velocidad, self.cilindrada)

c = Vehiculo("Rojo", 4, 5, 120, 2500)
print(Vehiculo)