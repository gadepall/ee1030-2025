import numpy as np

# Define the matrix from the image.
# The matrix is:
# [[2, 3, 0],
#  [3, 2, 0],
#  [0, 0, 1]]
A = np.array([[2, 3, 0],
              [3, 2, 0],
              [0, 0, 1]])

# Use numpy's linear algebra module (linalg) to find the eigenvalues.
# The function eigvals() returns the eigenvalues of a square matrix.
eigenvalues = np.linalg.eigvals(A)

# Print the original matrix and the calculated eigenvalues.
print("Matrix:")
print(A)
print("\nEigenvalues:")
# The output will be an array of the eigenvalues.
# For the given matrix, the eigenvalues are 5, -1, and 1.
# Note: The order of eigenvalues may vary.
print(eigenvalues)

