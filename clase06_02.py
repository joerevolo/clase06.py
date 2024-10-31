#-----------------------
#determinar el ganador
#-----------------------
#gana la segunda bolilla
#-----------------------
from random import randrange
alumnos= ['joe','daniel','gabriel','jose','franklin','brayan']

x = randrange(0,6)
print('Primer salida: ', alumnos[x])

y = randrange(0,6)
if (x==y):
    y = randrange(0,6)

print('ganador', alumnos[y])    