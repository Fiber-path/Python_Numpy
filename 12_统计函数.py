import numpy as np

a = np.arange(1, 101).reshape(10, 10)
print(np.sum(a))
b = np.array([1, 5, 43, 4, 64])
print(np.prod(b))
print(np.mean(b))     # 平均数
print(np.argmax(b))   # 返回最大值的索引 argmin则为最小值索引
print(np.unique(b))    # 删除重复数据，并排序