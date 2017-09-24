# Numpy Exampl_1
#
# array　　	        将输入数据转换为ndarray，类型可制定也可默认
# asarray　　	    将输入转换为ndarray
# arange	        类似内置range
# ones、ones_like　 根据形状创建一个全1的数组、后者可以复制其他数组的形状
# zeros、zeros_like	类似上面，全0
# empty、empty_like	创建新数组、只分配空间
# eye、identity	    创建对角线为1的对角矩阵

from numpy.random import randn

arr = randn(12).reshape(3, 4)

print(arr)
print(arr.shape)