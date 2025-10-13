import numpy as np

# Define the matrix
A = np.array([[1, 2],
              [3, 4]])

# Compute the determinant
det = np.linalg.det(A)
print("Determinant of A:", det)

# Check if inverse exists
if det == 0:
    print("Inverse does not exist (determinant is zero).")
else:
    # Compute the inverse
    A_inv = np.linalg.inv(A)
    print("Inverse of the matrix A is:\n", A_inv)

