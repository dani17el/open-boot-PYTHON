f = open('mi_archivo.txt', 'w')
f.write('Cree mi primer archivo de texto!\n')
f.close()

f = open('mi_archivo.txt', 'r+')
f.readline()
f.write('Es la segunda vez que escribo!\n')

f.seek(0)
print(f.read())
f.close()
