import numpy as np

# Define the matrix
A = np.array([[1, 2, 3],
              [2, 5, 7],
              [-2, -4, -5]])

# Compute inverse
A_inv = np.linalg.inv(A)

print("Inverse of the matrix is:")
print(A_inv)

# Verify by multiplying A and A_inv
identity_check = np.dot(A, A_inv)

print("\nVerification (A * A_inv):")
print(identity_check)

