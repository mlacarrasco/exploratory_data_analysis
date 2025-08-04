"""
 Miguel Carrasco (miguel.carrasco@udp.cl)
 version 1.0 (28/08/2019)
 
 Objetivo:
 1) Aplicar test Kruskal-Goodman Tau
 2) buscar si las variables son dependientes/independientes

   H0: Hipotesis Nula: Las variables son independientes
   H1: No puedo rechazar H0-> Las variables son dependientes
    
"""

import pandas as pd
import numpy as np
from scipy.stats import contingency

class GoodmanKruskalTau:
    """
    Implementación del tau de Goodman-Kruskal
    """
    
    @staticmethod
    def compute(x, y, direction='symmetric'):
        """
        Calcula tau de Goodman-Kruskal
        
        Parameters:
        x, y: arrays de variables categóricas
        direction: 'x_given_y', 'y_given_x', o 'symmetric'
        """
        # Convertir a arrays de pandas para manejo fácil
        df = pd.DataFrame({'x': x, 'y': y})
        
        # Tabla de contingencia
        table = pd.crosstab(df['x'], df['y'])
        
        if direction == 'y_given_x':
            return GoodmanKruskalTau._tau_y_given_x(table)
        elif direction == 'x_given_y':
            return GoodmanKruskalTau._tau_x_given_y(table)
        else:  # symmetric
            tau_yx = GoodmanKruskalTau._tau_y_given_x(table)
            tau_xy = GoodmanKruskalTau._tau_x_given_y(table)
            return {'tau_y_given_x': tau_yx, 'tau_x_given_y': tau_xy}
    
    @staticmethod
    def _tau_y_given_x(table):
        """Tau de Y dado X"""
        n = table.sum().sum()
        
        # Error total de Y
        row_totals = table.sum(axis=1)
        total_error_y = n - row_totals.max()
        
        # Error de Y dado X
        error_y_given_x = n - table.max(axis=1).sum()
        
        if total_error_y == 0:
            return 0
        
        tau = (total_error_y - error_y_given_x) / total_error_y
        return tau
    
    @staticmethod
    def _tau_x_given_y(table):
        """Tau de X dado Y"""
        return GoodmanKruskalTau._tau_y_given_x(table.T)

def TestIndependence(df, colX, colY):

        gk_tau = GoodmanKruskalTau()
        # extraemos la información de dos columnas
        X = df[colX].astype(str)
        y = df[colY].astype(str)

        dcc = gk_tau.compute(X, y)
        print(colX)

        # Interpretación de resultados
        if dcc['tau_y_given_x'] > 0:
                print(f"Las variables {colX} y {colY} son dependientes (tau > 0)")
        else:
                print(f"Las variables {colX} y {colY} son independientes (tau = 0)")

# Uso
       
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



