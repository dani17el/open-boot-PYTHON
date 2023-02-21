lista = ['a', 'b', 'c']
print(lista)
lista[0] = 'z'
print(lista)
lista[0] = 'a'
print(lista)

lista.append('x')
lista.append('y')
lista.append('z')
print(lista)
lista.append("patata")
print(lista)
lista.remove('c')
print(lista)

abc = ['a', 'b', 'c']
xyz = ['x', 'y', 'z']
abc.append(xyz)
print(abc)

unodostres = [1,2,3]
cuatrocincoseis = [4,5,6]

unodostres.append(cuatrocincoseis)
print(unodostres)

vacio = []
print(vacio)

vacio.append(cuatrocincoseis)
vacio.append(cuatrocincoseis)
vacio.append(cuatrocincoseis)
print(vacio)

diccionario = {
    "clave" : "valor",
    "clave2" : 15
}
print(diccionario)

print(diccionario['clave2'])

diccionario['clave2'] = 99
print(diccionario['clave2'])

print(diccionario)

diccionario = {'clave1':1, 'clave2':2, 'clave3':3, 'clave4':4}
print(diccionario)

import pprint
pprint.pprint(diccionario)

diccionario.pop('clave1')
print(diccionario)

elementoViejo = diccionario.pop('clave4')
print(elementoViejo)

lista = [1,2,3,1,2,3]
conjunto = {1,2,3,1,2,3}
print(lista)
print(conjunto)

a = {0,2,4,6,8}
b = {1,2,3,4,5}
print(a|b)
print(a&b)
print(a-b)
print(a^b)



numero = 5
cadenas = 'hola'
booleano = True
flotante = 5.5
listas = ['a','b','c','d']
tupla = ('a','b','c')
conjunto = {1,2,3,4,5,1,2,3,4,5}

mitexto = "hola, esto es un teXtO"
print(mitexto)

mitexto.capitalize()
print(mitexto.capitalize())

mitexto.title()
print(mitexto.title())

mitexto.lower()
print(mitexto.lower())

mitexto.upper()
print(mitexto.upper())

print(mitexto.replace('a','o'))
print(mitexto.replace('e','i'))
print(mitexto.find("esto"))
print(mitexto.split())
print(mitexto.split(','))

print(mitexto.replace(',', '').lower())
print(mitexto.replace(',', '').lower().split())

listaTexto = ['hola', 'esto', 'es','un', 'texto']
print(listaTexto)

print(' '.join(listaTexto))
print('-'.join(listaTexto))
print('*-*'.join(listaTexto))

mivarcompleta = ' '.join(listaTexto)
print(listaTexto)

print(mivarcompleta)

print(type(mivarcompleta))

texto = '5'
print(type(texto))
print(texto.isnumeric())

texto = 'a'
print(texto.isnumeric())

## comparacion: ==, !=, >, >=, <, <=
## identidad: is, is not
## membresia: in, not in
## bit: &,|,^,~, <<, >>



