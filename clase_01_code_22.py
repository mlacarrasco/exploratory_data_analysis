import pandas as pd

df = pd.read_csv("tasa.csv")
ordf = df.sort_values(by='2019')
my_range = range(1,len(df.index)+1)

plt.hlines(y=my_range, 
           xmin = ordf['2019'], 
           xmax = ordf['2020'], 
           color='grey', 
           alpha=0.8)

plt.scatter(ordf['2019'], my_range, color='skyblue', label='2019')
plt.scatter(ordf['2020'], my_range, color='green', label='2020')
plt.legend()

plt.show()

