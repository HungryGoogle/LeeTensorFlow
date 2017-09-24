# Print test

# 方式1
print("123", "456", "789", sep='-')

# 打印格式化字符串
a = "lee"
b = "test"
print("%s and %s." % (a, b))

# 打印格式化字符串
i1 = 1
i2 = 2
print("%d + %d = %d" % (i1, i2, i1 + i2))

# 打印到文件
print("打印到文件，请查看test.txt")
out = open(".\\log\\test.txt", "a")
print("123", file=out)
