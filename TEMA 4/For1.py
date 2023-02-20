#lista = [1,2,3,'a',5]
#tupla = (1,2,3,'c','d')
lista = ("hola","mensaje","adios")


longitud = len(lista)
print("La lista tiene", longitud, "items")

for numero in range(longitud):
    print(lista[numero])

if "mensaje" in lista:
    print("Encontre la palabra mensaje")

if "mensaje" not in lista:
    print("No hay palabra mensaje")




