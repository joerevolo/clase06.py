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
#n es una variable que va a tomar los valoers del rango entre 0 y 5
for n in range (0,6):
    if (x==y):
        y = randrange(0,6)
    else:
        exit   #sale del for del bucle 
print('ganador', alumnos[y])    
print('---------------')