import numpy as np

# Define matrices A and B
A = np.array([[1, -1, 0],
              [2,  3, 4],
              [0,  1, 2]])

B = np.array([[ 2,  2, -4],
              [-4,  2, -4],
              [ 2, -1,  5]])

# Compute inverses
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

# Define tolerance for floating point comparison
tol = 1e-9

# Check each condition
cond1 = np.allclose(A_inv, B, atol=tol)          # A^{-1} = B
cond2 = np.allclose(A_inv, 6*B, atol=tol)        # A^{-1} = 6B
cond3 = np.allclose(B_inv, B, atol=tol)          # B^{-1} = B
cond4 = np.allclose(B_inv, (1/6)*A, atol=tol)    # B^{-1} = (1/6)A

print("1) A^{-1} = B :", cond1)
print("2) A^{-1} = 6B:", cond2)
print("3) B^{-1} = B :", cond3)
print("4) B^{-1} = (1/6)A:", cond4)
