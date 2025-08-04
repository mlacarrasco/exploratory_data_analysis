import pandas as pd
import sklearn.utils
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

df = pd.read_csv('data/week5.csv')   # lee los datos del archivo csv
df.dropna(subset=['op','ag'], inplace=True)
data_df = df[["op","ag"]]

data_df= StandardScaler().fit_transform(data_df)
db = DBSCAN(eps=0.5, min_samples=5).fit(data_df)
labels = np.array(db.labels_)

colores =['red', 'blue', 'green', 'black']
fig, ax = plt.subplots()
for class_i in set(labels):
    index= labels==class_i
    ax.scatter(data_df[index,1], data_df[index,0], cmap='jet')
    
plt.show()
    
