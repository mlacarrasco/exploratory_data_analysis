import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({"ages": [65, 61, 25, 22, 27]}, 
                    index = ["Pedro","Juan","Sofía","Ale","Raúl"])

plotdata.plot(kind="bar")
plt.show()
