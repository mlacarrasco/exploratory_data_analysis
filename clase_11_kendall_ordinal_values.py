"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (07/06/2021)

 Objetivo:
 1) Mostrar la correalación entre múltiples variables 
 2) Emplear la biblioteca SeaBorn

"""

import pandas as pd
from pylab import rcParams
import seaborn as sb
from scipy.stats.stats import kendalltau
import matplotlib.pyplot as plt

# Parámetros de visualización
rcParams['figure.figsize'] = 14.7,8.27
sb.set_style('whitegrid')

# Import the data
african_crises = pd.read_csv("african_crises.csv")
african_crises.head()

# clases del problema
print(african_crises.banking_crisis.unique())

# el método Map permite cambiar los valores de una columna por otros.
african_crises['banking_crisis'] = african_crises['banking_crisis'].map({'crisis': 1, 'no_crisis': 0})
corr = african_crises.corr(method='kendall')

sb.heatmap(corr, 
           xticklabels=corr.columns.values, 
           yticklabels=corr.columns.values, 
           cmap="YlGnBu",
          annot=True)

plt.show()