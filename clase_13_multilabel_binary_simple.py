from sklearn.preprocessing import MultiLabelBinarizer
import pandas as pd


X = [['Male', 'Male', 'Other'], 
     ['Female', 'Female', 'Female'], 
     ['Female', 'Male' ]]

dataset = {'sex': X}

df = pd.DataFrame(data=dataset)
mlb = MultiLabelBinarizer()
datambl = mlb.fit_transform(df['sex'])
df_mbl = pd.DataFrame(datambl,columns=mlb.classes_, index=df.index)


#matriz de codificación de datos categóricos
print(df_mbl)
