#ESTE METODO ES EL ANTIGUO
# %d ES PARA NUMEROS
# %s ES PARA TEXTO O STRINGS
# %f ES PARA VALOR FLOTANTE (TRUE AND FALSE / DECIMALES)

numero = 5
texto = "quijote"
otromas = 1.23333

#print("El numero es %d y el texto es %s y tiene %f" % (numero,texto,otromas))

#print("Valor flotante: %.1f" % otromas)

#print("El numero es {} y el texto {} y tiene {}".format(numero,texto,otromas))

def suma(a,b):
    return a + b
txt = f'El numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}'
print(txt)