#intervalo de confianza
from  scipy import stats
from math import sqrt
import numpy as np

zLeft = stats.norm.ppf(0.025)
zRight = stats.norm.ppf(0.975)

print(zLeft)
print(zRight)

#datos del problema
X= 41.5
n = 10
sigma = 0.3

error = zRight* (sigma/sqrt(n))
ileft = X - error
iRight = X + error
print('Intervalo de confianza:')
print ('({:1.4} - {:1.4})'.format(ileft, iRight))
print('Margen de error :{:1.3%}'.format(error))

# numero de muestras para un error dado

new_error = 3/60 #minutos
n = ((zRight*sigma)/new_error)**2

print('Se requiere al menos de  {:1.3f} muestras para un error de {:2.0f} segundos'.format(n,new_error*60))





