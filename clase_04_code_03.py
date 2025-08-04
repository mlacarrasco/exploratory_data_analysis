import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

labl = {0:'Wine #1',1:'Wine #2', 2:'Wine #3'}

df = pd.read_csv('data/wine.csv')
wine_type = df['Class']-1
labels = wine_type.values
feature_names = df.columns[:-1].tolist()  # Get feature names excluding 'Class'

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

for wine_class in np.unique(labels):
    ix = wine_type == wine_class
    ax.scatter(X[ix], Y[ix], label=labl[wine_class], s=40)

scale_factor = 3  # Adjust this value to scale the arrows
for i, (comp_x, comp_y) in enumerate(pca.components_.T):
    ax.arrow(0, 0, comp_x * scale_factor, comp_y * scale_factor,
             head_width=0.1, head_length=0.1, fc='red', ec='red', alpha=0.6)
    ax.text(comp_x * scale_factor * 1.1, comp_y * scale_factor * 1.1,
            feature_names[i], fontsize=8, ha='center', va='center')
    


plt.xlabel("Primera Componente Principal",fontsize=14)
plt.ylabel("Segunda Componente Principal",fontsize=14)
plt.title("2-dimensional dataset con componentes principales")
ax.set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
