from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
data = [[0,0],[2,1], [2,2], [3,1], [4,2],[8,1]]
data = np.array(data)

print(data) 

n = data.shape[0]  # número de observaciones
p = data.shape[1]  # número de dimensiones
alpha = 0.05

# Para distancia de Mahalanobis, usar chi-cuadrado
chi2_crit = stats.t.ppf(1-alpha, p)
print('Umbral crítico (chi2):', chi2_crit)

# Centro y matriz de covarianza
centre = data.mean(axis=0)
mat_cov = np.cov(data.T)
mat_inv = np.linalg.inv(mat_cov)

print('Centro:', centre)
print('Matriz de covarianza:', mat_cov)

plt.figure()
distancias = np.empty(n)

# Calcular distancias
for i, row in enumerate(data):
    distancias[i] = (row-centre).T @ mat_inv @ (row-centre)

# Evaluar outliers FUERA del loop
for i, row in enumerate(data):
    if distancias[i] > chi2_crit:
        print(f"{row} es un outlier (distancia: {distancias[i]:.2f})")
        plt.scatter(row[0], row[1], color='red', s=100, label='Outlier')
    else:
        plt.scatter(row[0], row[1], color='blue', s=50, label='Normal')

plt.legend()
plt.title('Detección de Outliers - Distancia de Mahalanobis')
plt.show()