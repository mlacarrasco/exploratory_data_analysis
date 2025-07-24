import pandas as pd
import plotly.express as px
import plotly

#importante: instalar pip install plotly

#activar si se ejecuta en Google Colab
#plotly.io.renderers.default = 'colab'

import numpy as np

col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)

df = pd.DataFrame({'Age':col_1,
                   'Height': col_2})

fig = px.histogram(df, x="Age")
fig.add_trace(px.histogram(df, x="Height").data[0])
fig.show()


