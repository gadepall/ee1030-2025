import numpy as np

A = np.array([
    [1, 1, 1],
    [-1, 0, -0.2588],
    [0, 1, -0.9659]
], dtype=np.float32)

b = np.array([10, 0, 0], dtype=np.float32)

x = np.linalg.solve(A, b)
print("Solution [a b c]:", x)

