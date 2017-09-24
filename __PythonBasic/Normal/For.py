#
# 从0开始，打印到5
print("example 1 ------------------------------")
for i in range(5):
    print("i = " + str(i))

print("example 2 ------------------------------")
for i in range(5):
    for j in range(10):
        if i >= 2:
            continue
        if j > 1:
            break
        print("i = %d,j = %d" % (i, j))

# result
# example 1 ------------------------------
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4
# example 2 ------------------------------
# i = 0,j = 0
# i = 0,j = 1
# i = 1,j = 0
# i = 1,j = 1