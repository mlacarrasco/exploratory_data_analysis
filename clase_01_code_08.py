import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({ 	"pies_2018":[40, 12, 10, 26, 36],    				   
							"pies_2019":[19, 8, 30, 21, 38],    
							"pies_2020":[10, 10, 42, 17, 37] },    
                          index=["Dad", "Mam", "Bro", "Sis", "Me"])

plotdata[["pies_2018", "pies_2020"]].plot(kind="bar")

plt.title("Mince Pie Consumption Study")
plt.xlabel("Family Member")
plt.ylabel("Pies Consumed")
plt.show()
