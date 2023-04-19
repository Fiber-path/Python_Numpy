import numpy as np

#  创建一维0数组
a = np.zeros((6, 6), dtype=int)
print(a)

# 根据数组形状创建全为0的数组
b = np.zeros_like(a)
print(b)