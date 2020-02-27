-*- mode: org; -*-
import numpy as np


# 1.创建一个长度为 10 的随机数组并将最大值替换为 0
# np.argma()获得数组中最大值的索引
a = np.random.rand(10)
print(a)
a[np.argmax(a)] = 0
print(a)


# 2.创建一个范围在(0,1)之间的长度为 12 的等差数列
a = np.linspace(0, 1, 12)
print(a)
a = np.linspace(0, 1, 12, endpoint=False)
print(a)


# 3.创建一个每一行都是从 0 到 4 的 5*5 矩阵
alist = 5 * [i for i in range(5)]
a = np.array(alist).reshape((5, 5))
print(a)


# 4.给定一个 4 维矩阵，得到最后两维的和
:np_sum_extend:
# 不是返回整个矩阵的和，而是沿着最后两位求和
# 注意，最后两维指的是最高的两个维度，在这道题中，结果的维度应为(3, 2)?
# 为什么不是(4, 2)?
# np.sum()中指定维度(3, 2, 1, 0)?
# 因此，指定的最高维度应当用tuple表示为(3, 2)?
# https://blog.csdn.net/Shenpibaipao/article/details/91666136
# 解决：(3, 2, 1, 0)是维度从高到低的排列
# axis接受一个维度的索引或多个维度索引组成的tuple，按照最高维度展开
# 结果形状为(4, 2)，axis的参数为(3, 2),意味着按照从高到底，维度索引为3，2
:END:

a = np.arange(32).reshape((4, 2, 2, 2))
print(a)

b = np.sum(a, axis=(3, 2))
print(b)


# 5.随机生成一个 3x3 的矩阵，将矩阵的每一行都减去该行的平均值
a = np.random.rand(9).reshape((3, 3))
print(a)

for i in range(3):
    print(a[i].mean())
    a[i] = a[i] - a[i].mean()

print(a)


# 6.随机生成一个 3x3 的二维矩阵，交换该矩阵的第二行和第三行
a = np.random.rand(9).reshape((3, 3))
print(a)
a[[1, 2], :] = a[[2, 1],:]
print(a)
# 直接使用package/unpackage无效，需要对每一行的索引使用


# 7.对一个 5x5 的随机矩阵进行归一化（即将所有值缩放到[0, 1]范围内）
a = np.arange(25).reshape((5, 5))
print(a)
b = a.astype(np.float)
print(b)
# 百分比形式的归一化
total_sum = sum(b.flatten())
b = b / total_sum
print(b)

# 最大值形式的归一化
item_max_index = np.argmax(b)
item_max = b.flatten()[item_max_index]
b = b / item_max
print(b)
