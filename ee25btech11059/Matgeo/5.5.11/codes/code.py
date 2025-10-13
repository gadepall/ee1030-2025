import numpy as np

# Define the matrix A
A = np.array([[2, 0, -1],
              [5, 1, 0],
              [0, 1, 3]])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

print("Inverse of the matrix A is:")
print(A_inv)

