lista = ["hola", "mensaje", "adios"]

for palabra in lista:
    if palabra == "mensaje":
        print("Encuentro la palabra mensaje")
        break
else:
    print("No encuentro nada")