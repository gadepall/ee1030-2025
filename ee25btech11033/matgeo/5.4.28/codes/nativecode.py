import numpy as np

# Define the matrix
A = np.array([[2, 4],
              [-5, -1]])

# Compute inverse
A_inv = np.linalg.inv(A)

# Display result
print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)

