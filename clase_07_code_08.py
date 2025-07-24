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

df = pd.read_csv('tasaFertilidad2019vsGPD.csv')


fig, ax = plt.subplots(figsize=(8,8))

label = "Chile"
ids = df.loc[df["Pais"]=="Chile"]
xs=ids["TasaFertilidad"]
ys=ids["IngresoPerCapita"]

plt.annotate(label, # this is the text
            (xs,ys), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(0,10), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center

ax.grid()
ax.yaxis.set_major_formatter(fmtr)
for i in range(len(continents)):
  df_sel= df[df['Continente']==continents[i]]
  x = df_sel['TasaFertilidad']
  y = df_sel['IngresoPerCapita']
  ax.scatter(x,y, color=df_sel['Continente'].replace(colorbar), marker=None,label=continents[i], s=50)
 

ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')
ax.legend()



plt.show()