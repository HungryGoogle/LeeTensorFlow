### 一次性加载所有内容到内存
file = open(".\\log\\test.log", "r")
obj1 = file.read()
print("Way_1: \ncontent = " + obj1)


### Way2 read all lines
file = open("test.log", "r")
obj = file.readlines()
for line in obj:
    print("Way_2: line content = " + line)
