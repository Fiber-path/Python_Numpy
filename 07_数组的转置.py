import numpy as np

a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(a, '\n', a.T)
b = np.arange(1, 19).reshape(3, 6)
print(b.T)