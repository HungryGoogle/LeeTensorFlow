dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# 新增
dict['School']='hangzhou'
print(dict)

# 删除
del dict['School']
print(dict)

# 修改
dict['School']='豫州'
print(dict)

# 查询1
print("dict['Age']1: ", dict['Age'])
# print("dict['Age']2: ", dict['School2']) # error

# 查询2
print("dict['School2']: ",dict.get('School2', ""))

print(dict.keys())
print(dict.values())