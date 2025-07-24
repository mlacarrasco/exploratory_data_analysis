import pandas as pd
import matplotlib.pyplot as plt

plotdata = pd.DataFrame({"ages": [65, 61, 25, 22, 27]})

plotdata.plot(kind="bar")
