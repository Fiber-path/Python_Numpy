import numpy as np

# 设置随机种子，确定每次生产的随机数固定 (!!!!!! 全局适用 !!!!!!)
np.random.seed(1)
x = np.random.random()
print(x)

# 产生随机数组
y = np.random.random(size=(3, 4))
print(y)
print(y.shape)

# 产生随机整数
z = np.random.randint(1, 50, size=(5, 8))
print(z)
print(sum(list(z)))

# 正态分布
q = np.random.normal(0, 1, size=(4, 5, 3))    # size的参数意义：  几个 几行 几列
print(q)