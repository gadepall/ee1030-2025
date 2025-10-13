import numpy as np

A = np.array([
    [2, -1, 1],
    [-1, 2, -1],
    [1, -1, 2]
], dtype=float)

A2 = np.dot(A, A)
temp = A2 - 6*A + 9*np.eye(3)
Ainv = temp / 4.0

print("The inverse matrix A^{-1} is:")
print(Ainv)

print("Check A * A^{-1} = I:")
print(np.dot(A, Ainv))
