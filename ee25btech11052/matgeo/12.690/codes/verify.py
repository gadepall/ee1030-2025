import numpy as np


x = 10.0

# Define the matrix A using the calculated value of x
A = np.array([[x, -3.0],
              [3.0, 4.0]])

# Use numpy's linear algebra module (linalg) to find the eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Print the original matrix
print("Matrix A:")
print(A)

# Print the calculated eigenvalues
print("\nThe eigenvalues of the matrix are:")
print(eigenvalues)
print("Hence, our answer is correct as they are repeated")


