"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias

 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (17/06/2021)
 
 Objetivo:
 1) Transformar un archivo de canasta de compras en transacciones
 2) Transformar las trasacciones en una matriz tipo Dummy (unos y ceros)
 3) emplear algoritmo Apriori sobre transacciones
 4) Construir reglas de asociación
  
  definiciones en:
  https://michael.hahsler.net/research/recommender/associationrules.html
  enjoy!
"""

from numpy import record
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
 
#los datos no deben tener encabezado
basket = pd.read_csv('data/store_data.csv', header=None)



# reemplazamos los NaN con un cero
basket.fillna(0,inplace=True)
print(basket.head())

# Generamos una lista de transacciones para el algoritmo Apriori
transactions = []
for i in range(0,len(basket)):
    transactions.append([str(basket.values[i,j]) for j in range(0,20) if str(basket.values[i,j])!='0'])

# Generamos una matriz con unos y ceros de las transacciones
TE = TransactionEncoder()
table = TE.fit_transform(transactions)
df_mbl = pd.DataFrame(table, columns=TE.columns_, index=basket.index)

# empleamos el algoritmo Apriori para encontrar las cadenas con soporte minimo
frequent_itemsets = apriori(df_mbl, min_support=0.03, use_colnames=True)
print (frequent_itemsets)

# empleamos las reglas de asociación sobre los items más frecuentes
rules_lift = association_rules(frequent_itemsets, metric="lift", min_threshold=0.8)
print (rules_lift)
df_results = pd.DataFrame(rules_lift)
df_results.to_csv('resultados.csv')

