# ones 和 zeros用法大致相同
import numpy as np

print('----------------ones函数-----------------')
#  创建一维0数组
a = np.ones((6, 6), dtype=int)
print(a)

# 根据数组形状创建全为0的数组
b = np.ones_like(a)
print(b)

# 改变数组形状
c = np.ones((1, 24), dtype=int).reshape(6, 4)
print(c, c.shape)

print('--------------empty函数--------------')
# empty函数创建数组
dd = np.array([1, 5, 6, 3, 7])
d = np.empty(10, int)
np.add(dd, 56, out=d[5:])
print(d)

print('--------------full函数与full_like函数----------------')
e = np.full((3, 4), 5)
print(e)

eee = np.array([4, 6, 46, 1, 3, 465, 4])
ee = np.full_like(eee, 45, dtype=int)
print(ee)

print('-------------eye函数创建单位矩阵------------')
qq = np.eye(5, dtype=int)
print(qq)

print('-------------linspace函数创建等差数列------------')
x = np.linspace(2, 30, num=15, endpoint=True, retstep=True, dtype=float)
print(x)


print('-------------linspace函数创建等比数列------------')
xx= np.logspace(0, 4, num=5, base=2, endpoint=True, dtype=int)
print(xx[1:4])
print(np.logspace(0, 4, num=5, base=10, dtype=int))
