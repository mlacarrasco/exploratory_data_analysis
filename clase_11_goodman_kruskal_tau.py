"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias

 Miguel Carrasco (miguel.carrasco@uai.cl)
 version 1.0 (28/08/2019)
 
 Objetivo:
 1) Aplicar test Kruskal-Goodman Tau
 2) buscar si las variables son dependientes/independientes

   H0: Hipotesis Nula: Las variables son independientes
   H1: No puedo rechazar H0-> Las variables son dependientes
    
"""
from GKtau import GKtau
import numpy as np
import pandas as pd

def TestIndependence(df, colX, colY):

        # extraemos la información de dos columnas
        X = df[colX].astype(str)
        y = df[colY].astype(str)

        gk, p= GKtau(X, y)
        print(colX, gk, p)

       
#////////////////////////////////
# PROGRAMA PPAL
df = pd.pandas.read_csv("titanic.csv")
print(df.dtypes )

#Caracteristicas de la BD
testColumns = ['Embarked','Cabin','Pclass','Sex','Ticket','Age','Name']
for var in testColumns:
    # comparamos cada característica con la clase Survived
    # para evaluar si son independientes
    TestIndependence(df, var, "Survived" )  

