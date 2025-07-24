import numpy as np
from scipy import stats
from math import sqrt

n= 16   #número de datos
alpha = 0.05   #nivel de confindencia

t_crit = stats.t.ppf(1-alpha/n, n-2)

G_crit = ((n-1)/ sqrt(n)) * sqrt( t_crit **2/ (n-2+t_crit**2))

print("G_crit:", G_crit)

data = np.array([5, 14, 15, 15, 19, 17, 16, 20, 22, 8, 21, 28, 11, 9, 29, 40])

G_test = abs((data-np.mean(data)))/np.std(data)



test_grubbs = np.where(G_test > G_crit)
print("outliers:", data[test_grubbs])

