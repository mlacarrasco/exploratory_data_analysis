import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

labl={0:'Wine #1',1:'Wine #2', 2:'Wine #3'}

df= pd.read_csv("wine.csv")
wine_type = df['Class']-1
labels=wine_type.values

df.drop('Class',axis='columns', inplace=True)

scaler = StandardScaler()
scaler.fit(df) 
X_scaled = scaler.transform(df)

pca = PCA(n_components = 2)
pca.fit(X_scaled) 

X_pca = pca.transform(X_scaled)

expl = pca.explained_variance_ratio_

print('suma:',sum(expl[0:2]))

X = X_pca[:,0]
Y = X_pca[:,1]

fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
plt.grid(alpha=0.3)

for l in np.unique(labels):
    
    ix = wine_type == l
    ax.scatter(X[ix],Y[ix],label=labl[l],s=40)

for i, comp in enumerate(pca.components_):
    
    plt.plot([0, comp[0]], [0, comp[1]],
	      label=f"Componente {i}", 
             linewidth= 5,
             color = f"C{i + 2}") 

plt.xlabel("First Principal Component",fontsize=14)
plt.ylabel("Second Principal Component",fontsize=14)
plt.title("2-dimensional dataset with principal components")
plt.legend()
plt.show()
