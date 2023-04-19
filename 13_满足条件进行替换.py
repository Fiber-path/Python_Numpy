import numpy as np

a = np.arange(1, 17).reshape(4, 4)
print(a)
print('--------------------------')
np.place(a, 9 > a, 0)
print(a)
np.place(a, a > 14, 0)
print(a)

# 指定索引进行替换   put()函数
np.put(a, [5], 22)
print(a)