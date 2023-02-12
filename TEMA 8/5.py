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

cadena = "         en un lugar de la manchA"
print(cadena)
print(cadena.rstrip())
#funcion split hace un string en una lista, palabra por palabra
print(cadena.split())

print(cadena.startswith("   "))
print(cadena.endswith("manchA"))