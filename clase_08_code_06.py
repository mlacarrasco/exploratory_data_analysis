import matplotlib.pyplot as plt
import numpy as np

N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 300, size=N)

fig, ax = plt.subplots(figsize=(8,8))
scatter = ax.scatter(x, y, marker='.', s=s, c=c)

ax.grid(alpha =0.3)

legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")
plt.show()
