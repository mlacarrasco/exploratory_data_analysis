"""
 Miguel Carrasco (miguel.carrasco@udp.cl)
 version 1.0 (07/06/2021)

 Objetivo:
 1) Calcular la correlación de Kendall-Tau entre dos variables
 2) Mostrar los valores estadisticos

"""

import scipy.stats as stats

# data
x1 = [12, 2, 1, 12, 2]
x2 = [1, 4, 7, 1, 0]

# evaluación entre dos variables
tau, p_value = stats.kendalltau(x1, x2)
print('Tau:',tau)
print('P-value',p_value)