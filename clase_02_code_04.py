import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rand_values = np.random.rand(50) * 100
df = pd.DataFrame({'data':rand_values })

fig = plt.figure(figsize=(6,8))

ax = df.plot.hist(bins=12, alpha=0.5)

plt.show()
