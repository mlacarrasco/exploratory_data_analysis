import matplotlib.pyplot as plt

fig = plt.figure()

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]

plt.bar(langs,students)

plt.show()
