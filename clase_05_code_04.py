import pandas as pd

plotdata = pd.DataFrame({"ages": [65, 61, 25, 22, 27]})

plotdata.plot(kind="bar")
