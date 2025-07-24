import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid")


col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age':col_1,
                   'Height': col_2})

plt.figure(figsize=(8,8))

ax = sns.violinplot(data=df, split=True, inner="quartile")
plt.show()
