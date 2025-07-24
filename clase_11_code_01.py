from scipy import stats
from math import sqrt

# Hipotesis Nula (Ho)
Ho = 100
sigma = 5   #(desviación estandar poblacional)

# Hipotesis Alternativa (Ha)
Ha = 101.5
n = 40

# Error estandar de la media
err_media= (sigma/sqrt(n))

# calculo de Z (desviación estándar Normal)
z_scores = (Ha-Ho)/ err_media
print('Z score {:2.3}'.format(z_scores))


p_values = stats.norm.sf(abs(z_scores)) #one-sided
print('P-value:{:1.2%}'.format(p_values))