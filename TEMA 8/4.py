class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # funcion str ocaciona que se imprima directamente salidas informales
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi precio {self.precio}"

    # funcion repr ocaciona salidas tecnicas
    def __repr__(self):
        #return f'Potato({self.nombre},{self.precio})'
        return self.__str__()

#esto me muestra todas las funciones que puedo usar
#import pprint
#pprint.pprint(dir(''))

cadena = "en un lugar de la manchA"
numero = 'a5'

print(numero.isalpha())

print(cadena.title())
print(cadena.count('a'))
print(cadena.lower())
print(cadena.lower().count('a'))
print(cadena.upper())