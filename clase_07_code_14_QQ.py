import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

mu= 75
sigma = 6

s = np.random.normal(loc = mu, scale = sigma, size= 40)   
print(np.sort(s))

stats.probplot(s, dist="norm", plot=plt)
plt.show()

count, bins, ignored = plt.hist(s, 14, density=True)

plt.plot(bins, 
          1/(sigma*np.sqrt(2*np.pi)) * np.exp(- (bins-mu)**2/(2*sigma**2)),
          linewidth = 2, 
          color='r')

plt.show()

