import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch

colorbar ={"Africa":'k', 
  "Asia":'y', 
  "North America":'r', 
  "Europe":'b', 
  "Oceania":'g', 
  "South America":'m'}


def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

x = df['TasaFertilidad']
y = df['IngresoPerCapita']

fig, ax = plt.subplots(figsize=(8,8))
ax.grid()
ax.yaxis.set_major_formatter(fmtr)
ax.scatter(x,y, color=df['Continente'].replace(colorbar) ,marker='.', s=60)
ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')
plt.legend(
    [
	    Patch(facecolor=colorbar['Africa']),
     	Patch(facecolor=colorbar['Asia']),
      Patch(facecolor=colorbar['North America']),
      Patch(facecolor=colorbar['Europe']),
      Patch(facecolor=colorbar['Oceania']),
      Patch(facecolor=colorbar['South America']),

    ], 
    ["Africa", "Asia", "North America", "Europe", "Oceania", "South America"],
    title = "Continents"
)

plt.show()