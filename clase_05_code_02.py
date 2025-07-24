import matplotlib.pyplot as plt

fig = plt.figure()

data = [[30, 25, 50, 20],
        [40, 23, 51, 17],
        [35, 22, 45, 19]]

X = np.arange(4)


plt.bar(X + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, data[2], color = 'r', width = 0.25)

plt.legend(labels=['CS', 'IT', 'CS/TC'])

plt.show() 
