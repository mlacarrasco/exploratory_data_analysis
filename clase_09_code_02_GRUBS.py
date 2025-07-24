import numpy as np
from outliers import smirnov_grubbs as grubbs

data = np.array([5, 14, 15, 15, 19, 17, 16, 20, 22, 8, 21, 28, 11, 9, 29, 40])

print("buscando en ambos lados")
a= grubbs.test(data, alpha=.05)
print(a)

print("buscando en el lado mínimo")
b= grubbs.min_test(data, alpha=.05)
print(b)

print("buscando en el lado maximo")
c= grubbs.max_test(data, alpha=.05)
print(c)

indices= grubbs.max_test_indices(data, alpha=.05)
print(indices)

valores= grubbs.max_test_outliers(data, alpha=.05)
print(valores)
