import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch

def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

colorbar ={"Africa":'k', "Asia":'y', "North America":'r', "Europe":'b', "Oceania":'g', "South America":'m'} 
markerlist =['.','^', '+', 's', 's', '*'] 
continents =["Africa", "Asia", "North America", "Europe", "Oceania", "South America"] 
fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

fig, ax = plt.subplots(figsize=(8,8))
ax.yaxis.set_major_formatter(fmtr)

for i in range(len(continents)):
  df_sel= df[df['Continente']==continents[i]]
  x = df_sel['TasaFertilidad']
  y = df_sel['IngresoPerCapita']
  ax.scatter(x,y, color=df_sel['Continente'].replace(colorbar), marker=None,label=continents[i], s=50)
 
ids = df.loc[df["Pais"]=="Chile"]
xs = ids["TasaFertilidad"]
ys = ids["IngresoPerCapita"]
plt.annotate("Chile", # este es el texto a mostrar
            (xs,ys), # este es el punto a etiquetar
            textcoords="offset points", # cómo posicionar el texto
            xytext=(0,0), # distancia desde el texto hasta los puntos (x,y)
            size = 15,
            ha='left') # la alineación horizontal puede ser izquierda, derecha o centro

ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer (log 2)')
ax.set_ylabel('Promedio de per cápita, en miles de US$ (log 10)')
ax.legend()
plt.xscale('log', base=2)
plt.yscale('log', base=10)
ax.grid(alpha=0.3, which="both", ls="-")

plt.show()