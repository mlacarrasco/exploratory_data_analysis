"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.1 (07/06/2021)

 Objetivo:
 Calcular la correlación de spearman's entre dos variables
"""
import matplotlib.pyplot as plt
from numpy.random import rand
from numpy.random import seed
from scipy.stats import spearmanr, pearsonr

# seed random number generator
seed(1)

# generación de datos
data1 = rand(1000) * 20
data2 = data1 + (rand(1000) * 10)

# plot
plt.scatter(data1, data2)
plt.show()


# calculate spearman's correlation
coef, p = spearmanr(data1, data2)
print('Spearmans correlation coefficient: %.3f' % coef)
print('p-value', p)
#////////////////////////////////
#Interpretacion con nivel de significancia
alpha = 0.05 
if p <= alpha:
	print('Muestras están correlacionadas (reject H0) p={:.3}'.format(p))
else:
	print('Muestras no están correlacionadas (fail to reject H0) p={:.3}'.format(p))

