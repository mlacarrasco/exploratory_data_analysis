import pandas as pd
import numpy as np

df= pd.read_csv("wine.csv")
print(df.var())

X = np.array(df['Proline'])
Y = np.array(df['Magnesium'])

labl={0:'Wine #1',1:'Wine #2', 2:'Wine #3'}
wine_type = df['Class']-1
labels = wine_type.values

fig,ax=plt.subplots(figsize=(8,8))
for l in np.unique(labels):
    ix= wine_type == l 
    ax.scatter(X[ix],Y[ix],label=labl[l])

plt.xlabel('Proline');plt.ylabel('Magnesium')
plt.legend()
plt.show()
