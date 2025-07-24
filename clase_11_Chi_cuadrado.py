"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias

 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (28/08/2019)
 
 Objetivo:
 1) Aprender a utilizar una tabla de crosstab
 2) buscar si las variables son dependientes/independientes

   H0: Hipotesis Nula: Las variables son independientes
   H1: No puedo rechazar H0-> Las variables son dependientes
    
"""
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import numpy as np

#////////////////////////////////
#         | SUV | Sport Car | suma
# Hombres |  21 |  39       | = 60   
# Mujeres | 135 |  45       | = 180

#         | SUV (*)     | Sport Car    |
# Hombres |21/60=0.35   |  39/60=0.65  | = 1   
# Mujeres |135/180= 0.75| 45/180= 0.25 | = 1

#(la proporcion es distinta, por lo tanto no se puede asumir independencia)
   
table = [
	[21, 39],   
	[135, 45]
	]

TA = np.array(table)
X= TA[:,0]
Y= TA[:,1]

# Calculamos la tabla de contingencia según Chi2
print("Valores Observados:\n",table)
stat, p, dof, expected = chi2_contingency(table)


print("\nValores Esperados:\n",expected)
print('Grados de Libertad:%d' % dof)

#////////////////////////////////
#Interpretacion con umbral crítico

prob = 0.95 # nivel de confianza

critical = chi2.ppf(prob, dof)
print('Probabilidad={:.1%}, critical={:.3f}, estadístico={:.3f}'.format(prob, critical, stat))

if abs(stat) >= critical:
	print('Dependent (rechazar H0)')
else:
	print('Independent (fallamos en rechazar H0)')


print()
#////////////////////////////////
# Interpretacion a través de  p-value

# nivel de significancia
alpha = 1.0 - prob  

print('significancia={:.2}, p={:.4}'.format(alpha, p))
if p <= alpha:
	print('Dependientes (rechazar H0)')
else:
	print('Independientes (fallamos en rechazar H0)')
