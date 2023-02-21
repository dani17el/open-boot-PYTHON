class Vehiculo():

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color{}, Ruedas{}, Puertas{}".format(self.color,self.ruedas,self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, Ruedas {}, Puertas {}, Velocidad {} km/h, Cilindrada {} cc".format(self.color,self.ruedas,
                                                                        self.puertas,self.velocidad,self.cilindrada)

coche = Coche("Rojo", 4, 5, 120, 2500)
print("Las caracteristicas del coche son:")
print(coche)