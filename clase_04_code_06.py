import matplotlib.pyplot as plt
import numpy as np

N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 300, size=N)

fig, ax = plt.subplots(figsize=(8,8))
scatter = ax.scatter(x, y, marker='.', s=s, c=c)

ax.grid(alpha =0.3)

#scatter.legend_elements() es una tupla que contiene dos elementos: 
# 1. Un array con los colores únicos
# 2. Un array con los tamaños únicos
# Usamos estos arrays para crear dos leyendas diferentes
handles, labels = scatter.legend_elements(prop="colors", alpha=0.6)

# La leyenda de colores muestra las clases de vino
legend1 = ax.legend(handles, labels, loc="lower left", title="Classes")
ax.add_artist(legend1)

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")
plt.show()
