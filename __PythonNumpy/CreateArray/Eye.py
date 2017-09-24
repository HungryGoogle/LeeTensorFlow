import numpy as np

print("Example_1.1------------------------------")
d = np.eye((3))
print(d)

print("Example_1.2------------------------------")
d = np.eye((3), dtype=int)
print(d)

print("Example_1.3------------------------------")
d = np.eye(3, k=1, dtype=int)
print(d)

print("Example_1.4------------------------------")
d = np.eye(3, k=2, dtype=int)
print(d)