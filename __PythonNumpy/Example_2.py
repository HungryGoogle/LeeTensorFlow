import numpy as np


print ("\nExmaple_1------------------------")
arr = np.arange(6).reshape((2,3))
print(arr)
print('\n')
print(arr.T)


print ("\nExmaple_2------------------------")
arr = np.arange(24).reshape((2,3,4))
print (arr)

print ("\n Exmaple_3.1 ------------------------")
arr = np.arange(4).reshape((2,2))
print (arr)

print ("\n Exmaple_3.2 ------------------------")
print (arr + arr)

print ("\n Exmaple_3.3 ------------------------")
print (arr * arr)

print ("\n Exmaple_3.4 ------------------------")
print (arr * 2)