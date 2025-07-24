import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('data/week6.csv')
my_range = [1]*len(data.index)

fig  = plt.figure(figsize=(10,2))

ax = fig.gca()
ax.get_yaxis().set_visible(False)

plt.scatter(data['co'],my_range, color='blue', label='Compras')

plt.title("Distribución de compras por año")
plt.xlabel("Promedio de compra por cliente")
plt.show()
