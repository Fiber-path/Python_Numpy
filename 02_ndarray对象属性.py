import numpy as np

# 创建一维数组
a1 = np.array([1, 5, 4, 3, 4, 3, 64])
print(a1)
# 创建二维数组
a2 = np.array([[3, 4, 6, 3, 4, 9, 4], [7, 8, 9, 6, 4, 2, 3]])
print(a2)

# 创建三维数组
a3 = np.random.randn(2, 3, 4)
print(a3)

# 显示数组的秩
print(a1.ndim, a2.ndim, a3.ndim)

# 显示数组的元素个数
print(a1.size, a2.size, a3.size)

# 显示数组形状
print(a1.shape, a2.shape, a3.shape)
