import numpy as np
import matplotlib.pyplot as plt


mu = 200
sigma = 25
n_bins = 50

x = np.random.normal(mu, sigma, size=100)

fig, ax = plt.subplots(figsize=(8, 4))

ax.grid(True)
ax.hist(x)
ax.set_title('Rainfall histogram (mm)')

plt.show()
