import numpy as np
import matplotlib.pyplot as plt


spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * - 100

data = np.concatenate((spread, center, flier_high, flier_low))

fig = plt.figure(figsize=(10,6))

plt.boxplot(data)
plt.show()