import numpy as np

T = np.array([33.9, 35.5, 48.5, 74.4, 80.8])
V = np.array([1.75, 1.80, 1.86, 1.89, 1.92])

# 1. Construct the Design Matrix X for the quadratic model: [1, T, T^2]
X = np.column_stack([np.ones(len(T)), T, T**2])

# 2. The Response Vector C is the voltage V
C = V

# 3. Calculate the components for the normal equations:
# X^T * X and X^T * C
XTX = X.T @ X
XTC = X.T @ C

# 4. Solve the system of linear equations (normal equations) for the coefficients n:
# n = (X^T * X)^-1 @ (X^T * C)
n = np.linalg.solve(XTX, XTC)

# Extract the coefficients
n0, n1, n2 = n

print(f"n0: {n0}")
print(f"n1: {n1}")
print(f"n2: {n2}")