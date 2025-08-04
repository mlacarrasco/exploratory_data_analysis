import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/wine.csv')
df.drop('Class', axis='columns', inplace=True)

correlation_mat = df.corr()

fig = plt.figure(figsize=(10,10))

sns.heatmap(correlation_mat, annot = True)
plt.show()
