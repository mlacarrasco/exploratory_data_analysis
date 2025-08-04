import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch
import seaborn as sb

def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

colorbar ={"Africa":'r', "Asia":'y', "North America":'c', "Europe":'g', "Oceania":'b', "South America":'m'} 
fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

xs = np.log2(df['TasaFertilidad'])
ys = np.log10(df['IngresoPerCapita'])

fig, ax = plt.subplots(figsize=(8,8))
ax.grid()
ax.yaxis.set_major_formatter(fmtr)
sb.regplot(x = xs, y =ys, data = df, ci=95, order =1)
ax.scatter(xs,ys, color=df['Continente'].replace(colorbar), marker='.', s=210)
ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer (log2)')
ax.set_ylabel('Promedio de per cápita, en miles de US$ (log10)')
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