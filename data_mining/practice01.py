-*- mode: org; -*-
import numpy as np


# 1.����һ������Ϊ 10 ��������鲢�����ֵ�滻Ϊ 0
# np.argma()������������ֵ������
a = np.random.rand(10)
print(a)
a[np.argmax(a)] = 0
print(a)


# 2.����һ����Χ��(0,1)֮��ĳ���Ϊ 12 �ĵȲ�����
a = np.linspace(0, 1, 12)
print(a)
a = np.linspace(0, 1, 12, endpoint=False)
print(a)


# 3.����һ��ÿһ�ж��Ǵ� 0 �� 4 �� 5*5 ����
alist = 5 * [i for i in range(5)]
a = np.array(alist).reshape((5, 5))
print(a)


# 4.����һ�� 4 ά���󣬵õ������ά�ĺ�
:np_sum_extend:
# ���Ƿ�����������ĺͣ��������������λ���
# ע�⣬�����άָ������ߵ�����ά�ȣ���������У������ά��ӦΪ(3, 2)?
# Ϊʲô����(4, 2)?
# np.sum()��ָ��ά��(3, 2, 1, 0)?
# ��ˣ�ָ�������ά��Ӧ����tuple��ʾΪ(3, 2)?
# https://blog.csdn.net/Shenpibaipao/article/details/91666136
# �����(3, 2, 1, 0)��ά�ȴӸߵ��͵�����
# axis����һ��ά�ȵ���������ά��������ɵ�tuple���������ά��չ��
# �����״Ϊ(4, 2)��axis�Ĳ���Ϊ(3, 2),��ζ�Ű��մӸߵ��ף�ά������Ϊ3��2
:END:

a = np.arange(32).reshape((4, 2, 2, 2))
print(a)

b = np.sum(a, axis=(3, 2))
print(b)


# 5.�������һ�� 3x3 �ľ��󣬽������ÿһ�ж���ȥ���е�ƽ��ֵ
a = np.random.rand(9).reshape((3, 3))
print(a)

for i in range(3):
    print(a[i].mean())
    a[i] = a[i] - a[i].mean()

print(a)


# 6.�������һ�� 3x3 �Ķ�ά���󣬽����þ���ĵڶ��к͵�����
a = np.random.rand(9).reshape((3, 3))
print(a)
a[[1, 2], :] = a[[2, 1],:]
print(a)
# ֱ��ʹ��package/unpackage��Ч����Ҫ��ÿһ�е�����ʹ��


# 7.��һ�� 5x5 �����������й�һ������������ֵ���ŵ�[0, 1]��Χ�ڣ�
a = np.arange(25).reshape((5, 5))
print(a)
b = a.astype(np.float)
print(b)
# �ٷֱ���ʽ�Ĺ�һ��
total_sum = sum(b.flatten())
b = b / total_sum
print(b)

# ���ֵ��ʽ�Ĺ�һ��
item_max_index = np.argmax(b)
item_max = b.flatten()[item_max_index]
b = b / item_max
print(b)
