import numpy as np

A = np.array([[2, 1],
              [1, 3]])

v = np.array([1, 2])

inv = np.linalg.inv(A)
D = np.linalg.det(A)
print(D)

i = np.eye(5, 5)
print(i)