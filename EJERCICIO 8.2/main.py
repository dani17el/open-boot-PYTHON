from pickle import *


class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return self.marca + " " + self.color


c = Vehiculo("Honda", "Negro")
print(c)

f = open('vehiculo_objeto', 'w+b')
dump(c,f)

f.seek(0)
nuevo_c = load(f)

print(nuevo_c)
f.close()