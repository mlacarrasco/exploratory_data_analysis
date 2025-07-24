import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import pairwise_distances
from sklearn import manifold
from sklearn.preprocessing import StandardScaler

labl={0:'Wine #1',1:'Wine #2', 2:'Wine #3'}

df= pd.read_csv("wine.csv")
wine_type = df['Class']-1
labels=wine_type.values

df.drop('Class',axis='columns', inplace=True)
X_scaled = StandardScaler().fit_transform(df)

dist = pairwise_distances(X_scaled, metric='euclidean')
mds = manifold.MDS(n_components=2, dissimilarity="precomputed")
points = mds.fit_transform(dist)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()

for l in np.unique(labels):
    
    ix=  wine_type == l   
    ax.scatter(points[ix,0],points[ix,1], label=labl[l],s=40)

plt.legend()
plt.show()