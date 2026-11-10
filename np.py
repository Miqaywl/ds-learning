import numpy as np
a = np.array([2, -1])
b = np.array([-3, 4])


print(a + b)       # expect (-1, 3)
print(b - a)
print(3 * a)       # expect (6, -3)
print(2 * a - b)   # expect (7, -6)

print(np.linalg.norm(b))