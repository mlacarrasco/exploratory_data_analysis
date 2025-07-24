import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Patch
import seaborn as sns
from scipy import stats

def annotate(data, **kws):
    r, p = sp.stats.pearsonr(data['total_bill'], data['tip'])
    ax = plt.gca()
    ax.text(.05, .8, 'r={:.2f}, p={:.2g}'.format(r, p),
            transform=ax.transAxes)

def miles(x, pos):
    return '${:,.1f} M'.format(x*1e-3)

colorbar ={"Africa":'r', "Asia":'y', "North America":'c', "Europe":'g', "Oceania":'b', "South America":'m'} 
fmtr = matplotlib.ticker.FuncFormatter(miles)

df = pd.read_csv('tasaFertilidad2019vsGPD.csv')

df_sel = df[df['Continente']=='North America']
xs = df_sel['TasaFertilidad']
ys = df_sel['IngresoPerCapita']

slope, intercept, r_value, pv, se = stats.linregress(xs, ys)
print(r_value**2, intercept)

fig, ax = plt.subplots(figsize=(8,8))
ax.grid()
ax.yaxis.set_major_formatter(fmtr)
p= sns.regplot(x = xs, y =ys, order =1)

ax.scatter(xs,ys, marker='.', s=210)
ax.set_title('Niños por mujer vs Ingreso per cápita 2019')
ax.set_xlabel('Promedio de niños por mujer')
ax.set_ylabel('Promedio de per cápita, en miles de US$')
p.text(1.6,60000,str("R-value:{:1.3f}".format(r_value)))
plt.show()