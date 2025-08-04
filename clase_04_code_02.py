import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

labl = {0:'Wine #1',1:'Wine #2', 2:'Wine #3'}

#cargar el dataset
df = pd.read_csv("data/wine.csv")
#restamos 1 a la clase para que empiece en 0
wine_type = df['Class']-1
labels = wine_type.values

#quitar la columna 'Class' del dataframe
#esto es necesario para poder aplicar PCA
df.drop('Class',axis='columns', inplace=True)

scaler = StandardScaler()
scaler.fit(df) 
X_scaled = scaler.transform(df)

pca = PCA(n_components = 5)
pca.fit(X_scaled) 

X_pca = pca.transform(X_scaled)

expl = pca.explained_variance_ratio_

print('suma:',sum(expl[0:5]))

X = X_pca[:,0]
Y = X_pca[:,1]

fig, ax = plt.subplots(figsize=(10,10))

plt.grid(alpha=0.3)

for wine_class in np.unique(labels):

    ix = wine_type == wine_class
    ax.scatter(X[ix], Y[ix], label=labl[wine_class], s=40)

plt.xlabel("Primera Componente Principal",fontsize=14)
plt.ylabel("Segunda Componente Principal",fontsize=14)
plt.title("2-dimensional dataset con componentes principales")
plt.legend()
ax.set_aspect('equal')
plt.axis('square')
plt.show()
