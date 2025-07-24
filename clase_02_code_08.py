import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")


col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age':col_1,
                   'Height': col_2})


ax = sns.violinplot(x=df['Height'], split=True, inner="quartile")

plt.show()
