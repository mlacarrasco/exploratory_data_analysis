import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from sklearn.datasets import make_blobs
from pandas import DataFrame
import random


r_seed = 0
# Generate three 2D clusters totalling 1000 points 
X, y = make_blobs(n_samples=1000, centers=1, n_features=2, random_state=r_seed)
random.seed(r_seed)
random_pts = []

# Generate random noise points that could be or could not be close to the clustered neighborhoods
for i in range(50):
    random_pts.append([random.randint(-10, 10), random.randint(-10, 10)])

X = np.append(X, random_pts, axis=0)

df = DataFrame(dict(x=X[:,0], y=X[:,1]))
df.plot(kind='scatter', x='x', y='y')


x1= X[:,0]
x2= X[:,1]

data = np.stack((x1,x2),axis=0)
covariance_matrix = np.cov(data)

#calculating the mean
mean_values = [np.mean(x1),np.mean(x2)]

#multivariate normal distribution
model = multivariate_normal(cov=covariance_matrix,mean=mean_values)
data = np.stack((x1,x2),axis=1)

#finding the outliers
threshold = 1.0e-07
outlier = model.pdf(data).reshape(-1) < threshold

for boolean,i in enumerate(outlier):
  if i == True:
    print(data[boolean]," is an Outlier")