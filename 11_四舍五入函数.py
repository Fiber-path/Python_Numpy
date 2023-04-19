import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(1, 10, num=6, retstep=True)
b = np.linspace(1, 10, num=6)
c = np.linspace(1, 10, num=6)
print(a)
print(np.rint(b))
print(np.around(c, 2))  # 数组后面的值为正，四舍五入小数位，如果为负，则将小数点左边四舍五入
print(np.around(c, -1))
x = np.linspace(-15,15,200)
y = np.sin(x)
plt.plot(x, y)
plt.show()