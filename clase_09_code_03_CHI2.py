#codigo basado en 
#https://towardsdatascience.com/multivariate-outlier-detection-in-python-e946cfc843b3


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import chi2
from matplotlib import patches


# lectura de los datos
df= pd.read_csv('airquality.csv')


# seleccionamos dos columnas
df = df[['Ozone', 'Temp']]
df = df.dropna()
df = df.to_numpy()

fig = plt.figure()
plt.scatter(df[:,0], df[:,1], marker='o', color='blue', s=50)
plt.show()
# Matriz de covarianza
covariance  = np.cov(df , rowvar=False)

# Invertimos la matriz de convarianza 
covariance_pm1 = np.linalg.matrix_power(covariance, -1)

# Buscamos la media
centerpoint = np.mean(df , axis=0)

# Distancias entre el centro y cada punto
distances = []
for i, val in enumerate(df):
      p1 = val
      p2 = centerpoint
      distance = (p1-p2).T.dot(covariance_pm1).dot(p1-p2)
      distances.append(distance)
      
distances = np.array(distances)

# Punto de término de Distribución Chi-Square para detectar outlier.
cutoff = chi2.ppf(0.95, df.shape[1])

# Indices de Outliers
outlierIndexes = np.where(distances > cutoff )

print('--- Indices de Outlier ----')
print(outlierIndexes)

print('--- Observaciones ----')
print(df[ distances > cutoff , :])

# Dimensiones de la ellipse 
lambda_, v = np.linalg.eig(covariance)
lambda_ = np.sqrt(lambda_)

# Ellipse patch
ellipse = patches.Ellipse(xy=(centerpoint[0], centerpoint[1]),
                  width=lambda_[0]*np.sqrt(cutoff)*2, height=lambda_[1]*np.sqrt(cutoff)*2,
                  angle=np.rad2deg(np.arccos(v[0, 0])))
ellipse.set_facecolor('#0984e3')
ellipse.set_alpha(0.5)
fig = plt.figure()
ax = plt.subplot()
ax.add_artist(ellipse)
plt.scatter(df[: , 0], df[ : , 1], color= "blue", s=50)
plt.show()