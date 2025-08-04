import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cargar el dataset
df= pd.read_csv('data/wine.csv')
print(df.var())

#separar las variables
#X: Proline
#Y: Magnesium
#labels: Class (Wine type)
#Class: 1,2,3
X = np.array(df['Proline'])
Y = np.array(df['Magnesium'])

labl = {0:'Wine #1',1:'Wine #2', 2:'Wine #3'}

#convertir la clase a un valor entre 0 y 2
#Wine #1: 0, Wine #2: 1, Wine #3: 2
#esto es necesario para poder graficar
#la clase es la columna 'Class' del dataframe
#restamos 1 para que las clases empiecen en 0
wine_type = df['Class']-1
labels = wine_type.values


#graficar los datos
fig,ax=plt.subplots(figsize=(8,8))
for l in np.unique(labels):
    ix= wine_type == l 
    ax.scatter(X[ix],Y[ix],label=labl[l])

plt.xlabel('Proline');plt.ylabel('Magnesium')
plt.legend()
plt.show()
