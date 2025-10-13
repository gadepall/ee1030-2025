import numpy as np
A = np.array([[3, -3],
              [-3, 4]])
I = np.eye(2)

expr = -A @ A + 7*A - 3*I

det_value = np.linalg.det(expr)

print("Matrix A:\n", A)
print("Matrix (-A^2 + 7A - 3I):\n", expr)
print("Determinant =", det_value)

