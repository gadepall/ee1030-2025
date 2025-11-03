import numpy as np

A = np.array([[1, 0, 0], [3, 3, 0], [5, 2, 1]], dtype=np.float64)

B = np.linalg.inv(A)

print('The inverted matrix is: ')
print(B)
