"""
 Miguel Carrasco (miguel.carrasco@udp.cl)
 version 1.1 (07/06/2021)

 Objetivo:
 
 1) Buscar aquellas columnas que tengan más información 
 2) Seleccionar características con Chi-Square
    
   H0: Hipotesis Nula: Las variables son independientes
   H1: No puedo rechazar H0-> Las variables son dependientes
    
"""

import pandas as pd
from scipy.stats import chi2_contingency

#////////////////////////////////
# FUNCION
def print_chisquare_result(chi2,p, colX, alpha):
        result = ""
        
        #si p <= alpha, se rechaza H0 (hipótesis nula), significa que las variables dependientes
        # si p>alpha, no hay evidencia para rechazar H0, significa que las variables independientes
        if p<alpha:
            result="{0} is IMPORTANT for Prediction. p={1}".format(colX, p)
        else:
            result="{0} is NOT an important predictor. (Discard {0} from model, p={1})".format(colX, p)
        print(result)
  

#////////////////////////////////
# FUNCION      
def TestIndependence(df, colX, colY):

        # nivel de significancia
        alpha=0.05  

        # extraemos la información de dos columnas
        X = df[colX].astype(str)
        Y = df[colY].astype(str)
        
        # creamos una tabla cruzada
        df_Observed = pd.crosstab(Y,X)  

        chi2, p, dof, expected = chi2_contingency(df_Observed.values)

        print_chisquare_result(chi2,p, colX, alpha)


#////////////////////////////////
# PROGRAMA PPAL
df = pd.pandas.read_csv("data/titanic.csv")
print(df.dtypes )

#Caracteristicas de la BD
testColumns = ['Embarked','Cabin','Pclass','Sex','Ticket','Age','Name']
for var in testColumns:
    # comparamos cada característica con la clase Survived
    # para evaluar si son independientes
    TestIndependence(df, var, "Survived" )  

