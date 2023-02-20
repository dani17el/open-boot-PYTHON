from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #las clases abstractas necesita una implementacion y se coloca antes del metodo
    def sonido(self):
        pass

    def diHola(self): #las clases fuera de la abstraccion no necesita implementacion
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
p.sonido()
p.diHola()

p = Gato()
p.sonido()
p.diHola()