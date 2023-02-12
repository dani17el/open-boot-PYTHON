# r: lectura
# a: append
# w: escritura
# x: create

# t: texto
# b: binary

# +

f = open('/etc/passwd', 'r')
datos = f.readline()
datos = f.readline()
f.close()

print(datos)