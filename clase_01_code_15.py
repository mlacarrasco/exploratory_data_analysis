import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


data = pd.DataFrame({ 	"age":[48, 47, 10, 16, 18],    			               
						"gender":["M", "F","M", "F", "M"]},    
                      index=["Dad", "Mam", "Bro", "Sis", "Me"])

color = {"M": "#273c75", "F": "#44bd32"}

data["age"].plot(kind="bar", color=data['gender'].replace(color))

plt.legend(
    [
	Patch(facecolor=color['M']),
    Patch(facecolor=color['F'])
    ], 
    ["male", "female"]
)
plt.title("Family Age Distribution")
plt.xlabel("Family Member")
plt.ylabel("Age")
plt.xticks(rotation=45, horizontalalignment="center")
plt.tight_layout()
plt.show()