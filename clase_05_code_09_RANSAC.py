import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from scipy.stats import chi2
from matplotlib import patches


# lectura de los datos
df= pd.read_csv('data/airquality.csv')
# eliminamos filas con valores NaN
df.dropna(subset=['Ozone', 'Temp'], inplace=True)

df = df.to_numpy()

X= df[:,0].reshape(-1,1)
y= df[:,1]

# Fit line using all data
lr = linear_model.LinearRegression()
lr.fit(X, y)

#Modelo lineal robusto con algoritmo de RANSAC
ransac = linear_model.RANSACRegressor(min_samples=20)
ransac.fit(X,y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

#coeficientes beta0 y beta1
slope_ransac = ransac.estimator_.coef_
intercept_ransac =ransac.estimator_.intercept_

# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)

lw = 2
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
ax[0].scatter(X, y, color='red', marker='.')
ax[1].scatter(X[outlier_mask], y[outlier_mask], color='gold', marker='.',
            label='Outliers')
ax[1].scatter(X[inlier_mask], y[inlier_mask], color='blue', marker='.',
            label='Inliers')
ax[1].plot(line_X, line_y_ransac, color='cornflowerblue', linewidth=lw,
         label='RANSAC regressor')
ax[1].plot(line_X, line_y, color='navy', linewidth=lw, label='Linear regressor')
plt.legend()
plt.show()