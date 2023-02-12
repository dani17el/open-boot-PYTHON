f = open('mifichero.txt', 'w')
#f.write("datos\n")
#f.write("datos2\n")
lista = [
    'una linea\n',
    'dos lineas\n',
    'tres lineas\n'
]
f.writelines(lista)
f.close()