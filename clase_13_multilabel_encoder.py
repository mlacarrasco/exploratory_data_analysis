import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from mlxtend.frequent_patterns import apriori

#instalar mlxtend
#pip install mlxtend

dataset = {'A':[['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]}

df = pd.DataFrame(data=dataset)
#print(df)

mlb = MultiLabelBinarizer()
datambl = mlb.fit_transform(df['A'])
df_mbl = pd.DataFrame(datambl,columns=mlb.classes_, index=df.index)
#print(df_mbl)

frequent_itemsets = apriori(df_mbl, min_support=0.4, use_colnames=True)
#print (frequent_itemsets)

from mlxtend.frequent_patterns import association_rules

rules_lift = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
rules_conf = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print (rules_lift)
 
support = rules_lift[['antecedents','consequents','support','lift']]
confidence = rules_lift['confidence']

print(support)

