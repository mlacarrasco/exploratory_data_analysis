# generate related variables
import numpy as np
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
# calculate the Pearson's correlation between two variables
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler


# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1/2 + (10 * randn(1000) + 50)

data = np.vstack((data1, data2))
data = data.T
data = StandardScaler().fit_transform(data)

print(data)
print(data.shape)
# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data[:,0]), std(data[:,1])))
print('data2: mean=%.3f stdv=%.3f' % (mean(data[:,0]), std(data[:,1])))
# plot
pyplot.scatter(data[:,0], data[:,1])
pyplot.show()

# calculate Pearson's correlation
corr, t = pearsonr(data[:,0], data[:,1])
print('Pearsons correlation: %.3f' % corr)
print('t statistic (p-value):', t)