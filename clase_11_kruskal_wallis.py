"""
  Miguel Carrasco (miguel.carrasco@udp.cl)
 version 1.0 (28/08/2019)
 
 Objetivo:
 1) Aplicar test Kruskal-Wallis
 2) buscar si las variables son dependientes/independientes

   H0: Hipotesis Nula: Las variables son independientes
   H1: No puedo rechazar H0-> Las variables son dependientes
    
"""
from scipy import stats
import numpy as np
import pandas as pd

#////////////////////////////////
# FUNCION
def print_result(ss, p, alpha):
        result = ""
        
        #si p <= alpha, se rechaza H0 (hipótesis nula), significa que la media entre grupos son distintas. 
        # Advertencia: no sabemos cual de ellas difiere.

        # si p>alpha, no hay evidencia para rechazar H0, significa que la 
        # población de las medias entre todos los grupos son iguales
        if p<alpha:
            result="reject Null-Hypothesis."
        else:
            result="Fail to reject H0."
        print(result)
  
       
#////////////////////////////////
# PROGRAMA PPAL
# nivel de significancia
alpha=0.05  

df = pd.pandas.read_csv("titanic.csv")
print(df.dtypes )

#Caracteristicas de la BD
testColumns = ['Embarked','Cabin','Pclass','Sex','Ticket','Age','Name']
# comparamos cada característica con la clase Survived
# para evaluar son de medias distintas

# extraemos la información de dos columnas
Embarked = df['Embarked'].astype(str)
Cabin = df['Cabin'].astype(str)
Pclass = df['Cabin'].astype(str)
Sex = df['Cabin'].astype(str)

statistic, p_value = stats.kruskal(Embarked, Cabin, Pclass, Sex)
print_result(statistic, p_value, alpha)

