"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.1 (07/06/2021)

 Objetivo:
 Calcular la correlación de Pearson's correlation entre dos variables

"""
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# seed random number generator
seed(1)


# generación de datos
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# summarize
print('data1: mean={:.3f} stdv={:.3f}'.format(mean(data1), std(data1)))
print('data2: mean={:.3f} stdv={:.3f}'.format(mean(data2), std(data2)))

plt.scatter(data1, data2)
plt.xlabel('Data 1');plt.ylabel('Data 2');
plt.show()


#////////////////////////////////
# Resultados
corr, p = pearsonr(data1, data2)
print('Pearsons correlation: {:.3f}'.format(corr))
print('P-value t: {:.3e}'.format(p))

#////////////////////////////////
#Interpretacion con nivel de significancia
alpha = 0.05 
if p <= alpha:
	print('Muestras están correlacionadas (reject H0) p={:.3e}'.format(p))
else:
	print('Muestras no están correlacionadas (fail to reject H0) p={:.3e}'.format(p))
