import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


col_1 = np.random.rand(50) * 100
col_2 = np.random.rand(50) * 100+50

df = pd.DataFrame({'col_1': col_1,
                   'col_2': col_2})


df.plot.hist(bins=20, alpha=0.5, color=['blue', 'orange'])
plt.title('Histograma de dos distribuciones')
plt.show()
