import numpy as np
import matplotlib.pyplot as plt

menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

ind = np.arange(5)
width = 0.35

fig = plt.figure()

plt.bar(ind, menMeans, width, color = 'r')
plt.bar(ind, womenMeans, width, bottom=menMeans, color = 'b')

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))

plt.legend(labels=['Men', 'Women'])
plt.show()


