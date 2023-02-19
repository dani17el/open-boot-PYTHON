numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
def miFuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(miFuncion, numeros)
print(list(resultado))