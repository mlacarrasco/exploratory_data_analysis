import pandas as pd
import plotly.express as px

import numpy as np
#activar si se ejecuta en Google Colab
#plotly.io.renderers.default = 'colab'


col_1 = np.random.rand(500) * 80
col_2 = np.random.normal(150, 12, 500)
df = pd.DataFrame({'Age': col_1,
                   'Height': col_2})

fig = px.histogram(df, x="Age", title="Histograma del atributo edad")
fig.update_layout(title_x=0.5)  # This centers the title
fig.show()