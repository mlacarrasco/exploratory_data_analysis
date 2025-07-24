import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rand_values = np.random.rand(50) * 100
df = pd.DataFrame({'data':rand_values })


df.plot(kind='hist', bins=12, alpha=0.5, color='blue')
plt.show()
