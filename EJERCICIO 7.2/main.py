import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Es hora de ir a casa")
else:
    print("Queda {} horas y {} minutos para ir a casa".format(18-int(hora), 59-int(minutos)))

