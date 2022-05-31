import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])


c = np.add(a, b)
print(c)


c = np.subtract(a, b)
print(c)


c = np.multiply(a, b)
print(c)


c = np.divide(a, b)
print(c)


print(a.shape)

d = np.array(range(50)).reshape((10,5))
print(d)