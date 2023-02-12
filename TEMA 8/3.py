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

j1 = Juguete("Potato", 10.5)
j2= Juguete("Dino", 3.4)

print(j1)
print(j2)