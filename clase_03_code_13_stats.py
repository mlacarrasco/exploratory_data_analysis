import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch
import seaborn as sb


#instalar scipy y statsmodels si no están instalados  
#pip install scipy statsmodels
from scipy import stats
from statsmodels.formula.api import ols


colorbar ={"Africa":'r', 
           "Asia":'y', 
           "North America":'c', 
           "Europe":'g', 
           "Oceania":'b', 
           "South America":'m'} 

df = pd.read_csv('data/tasaFertilidad2019vsGPD.csv')

xs = np.log2(df['TasaFertilidad'])
ys = np.log10(df['IngresoPerCapita'])

dff = pd.DataFrame({'TasaFertilidad':xs, 'IngresoPerCapita':ys})

gradient, intercept, r_value, p_value, std_err = stats.linregress(xs,ys)
model = ols("IngresoPerCapita ~ TasaFertilidad", data=dff)
results = model.fit()
print(results.summary())
print(results.params)
print(results.rsquared)

print("Gradient:{} intercept:{}".format( gradient, intercept))
print("r_value:{} p_value:{}".format( r_value, p_value))

fig, ax = plt.subplots(figsize=(8,8))
ax.grid(alpha=0.3)
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