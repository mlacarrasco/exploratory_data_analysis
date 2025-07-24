import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('tasaFertilidad2019vsGPD.csv')

x = df['TasaFertilidad']
y = df['IngresoPerCapita']

fig = plt.figure(figsize=(8,8))
plt.grid( alpha = 0.3)

plt.scatter(x, y, color='g', s=100, marker='+' )

plt.xlabel('Tasa de Fertilidad')
plt.ylabel('Ingreso per Cápita')
plt.show()
