global i
i = 1


def hanu():
    global i
    i += 1

# 会调用错误
def hanu2():
    i += 1

hanu()
print("move counts =", i)

# hanu2()