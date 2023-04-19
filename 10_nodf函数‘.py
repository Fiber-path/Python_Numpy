import numpy as np

a = np.random.random(5)
b = a +1
print(b)
c = np.modf(b)
print(c)
print(c[0][2],c[1][2])