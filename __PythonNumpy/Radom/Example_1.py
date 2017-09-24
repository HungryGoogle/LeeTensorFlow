import numpy as np
# http://blog.csdn.net/vicdd/article/details/52667709
#

print("Example_1.1------------------------------")
# randint(low[, high, size]), return
result = np.random.randint(1,10, size=10)
print(result) # [0 1 0 0 1 1 0 0 1 0]

print("Example_1.2------------------------------")
# result float[0, 1)
result = np.random.random_sample()
print(result) # maybe 0.59809686223244

print("Example_1.3------------------------------")
# center 0
# width = 0.1
# new number 10
result = np.random.normal(0, 0.1, 10)
print(result)

# result
#[-0.22999211  0.0787427  -0.18554561 -0.13547081 -0.03976493  0.05435463
#  0.15561572 -0.03134273 -0.00062671 -0.05838184]

print("Example_1.3------------------------------")
#
arr = np.arange(10)
np.random.shuffle(arr)
print(arr) # maybe [1 5 0 3 9 8 2 4 7 6]

arr = arr.reshape(2,5)
print(arr)
# result
# [[1 5 0 3 9]
#  [8 2 4 7 6]]