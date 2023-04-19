import numpy as np

a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
b = np.array([9, 8, 7, 4, 5, 6]).reshape(2, 3)
aa = np.arange(1, 37).reshape(2, 3, 6)
bb = np.arange(201, 237).reshape(2, 3, 6)
# print(np.concatenate((a, b), axis=1))
# print(np.hstack((a, b)))  # 应该等价于axis=1
# print(np.vstack((a, b)))  # 应该等价于axis=0
# print(np.dstack((aa, bb)).shape)  # 应该等价于axis=2
