import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({ 	"age":[48, 47, 10, 16, 18],    			               
						"gender":["M", "F","M", "F", "M"]},    
                      index=["Dad", "Mam", "Bro", "Sis", "Me"])


color = {"M": "#273c75", "F": "#44bd32"}
data["age"].plot(kind="bar", color=data['gender'].replace(color))





