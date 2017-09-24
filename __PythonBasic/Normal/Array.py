#
# a.append(5) 追加5
# a.count(3) 统计，计数
# a.index() 索引，所在位置
# a.extend() 扩展
# a.insert(2,6) 第2个位置插入6
# a.pop() 删除最后一个
# a.remove() 删除指定名称
# a.reverse() 反转
# a.sort() 排序，数字在最前面。

a = [1,2,3,4,7,8,9,3]

# print array a
print(a)

# print number of 3 in array
print(a.count(3))

# remove all 3 in array
for i in range(a.count(3)):
    a.remove(3)  # 删除a列表里面所有5。
print(a)
