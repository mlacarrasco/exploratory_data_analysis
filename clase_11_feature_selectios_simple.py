"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.1 (07/06/2021)
 
 Objetivo:

 1) Seleccionar las características según un estadístico
 2) Mostrar el número de características calculadas por el selector
 
    
"""
# Carga bibliotecas
import seaborn as sns
import pandas as pd

import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2,f_regression, mutual_info_classif, RFE
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

#////////////////////////////////
#carga de datos: Modelo supervisado
iris = sns.load_dataset("iris")

# características del problema
X = iris[['sepal_length','sepal_width','petal_length', 'petal_width']]       

# columna contiene la clase (no aplica a todos los problemas)
y = iris['species']      

clusters = 3   # Define el numero de clusters

#////////////////////////////////
# GRAFICA
sns.pairplot(iris,hue='species')
plt.show()

#////////////////////////////////
# MODELO 1. Chi2
chi2_selector = SelectKBest(chi2, k=clusters)        # el valor de k controla el numero de caracteristicas
features1 = chi2_selector.fit_transform(X, y)
fit = chi2_selector.fit(X, y)
print("Modelo Chi2: ",fit.scores_)

#RESULTADOS
print('Numero original de características:', X.shape[1])
print('Numero reducido de características:', features1.shape[1])


#////////////////////////////////
# MODELO 2. Recursive Feature Elimination (RFE)
model = LogisticRegression(solver='lbfgs',max_iter=1000, multi_class='auto')
rfe = RFE(model, clusters)  
fit2 = rfe.fit(X, y)

print("Modelo Regresion Logistica: ",fit2.support_)
# Transformar el dataset
features2 = fit2.transform(X)
    