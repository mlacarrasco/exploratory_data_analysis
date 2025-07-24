import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

se = pd.Series( 3 * np.random.rand(4), 
                 index = ["a", "b", "c", "d"], 
                 name = "Serie")

print(df)

se.plot.pie( labels=["AA", "BB", "CC", "DD"],
             colors=["r", "g", "b", "c"],
             autopct="%.2f",
             fontsize=20,
             figsize=(8,6))

