"""
 Miguel Carrasco (miguel.carrasco@udp.cl)
 version 1.0 (07/06/2021)

 Objetivo:
 1) Calcular la correlación de kendall entre dos variables
 2) Mostrar la intepretación de los valores

"""

from numpy.random import rand
from numpy.random import seed
from scipy.stats import kendalltau
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# seed random number generator
seed(1)

# generación de datos aleatrios
data1 = (rand(1000) * 20).reshape(-1,1)
data2 = data1 + rand(1000).reshape(-1,1) * 10

# graficamos los datos
data_columnas = np.hstack((data1,data2))
df = pd.DataFrame(data_columnas,columns=['Data1','Data2'])
sb.pairplot(df)
plt.show()


#////////////////////////////////
# Resultados
# calcula la correlación de Kendall-Tau
coef, p = kendalltau(data1, data2)
print('Kendall correlation coefficient: {:.3}'.format(coef))

#////////////////////////////////
#Interpretación con nivel de significancia
alpha = 0.05 

if p <= alpha:
	print('Muestras están correlacionadas (reject H0) p={:.3}'.format(p))
else:
	print('Muestras no están correlacionadas (fail to reject H0) p={:.3}'.format(p))