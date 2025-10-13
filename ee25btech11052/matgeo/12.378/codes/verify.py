import numpy as np

# Define the matrix from the document [cite: 5]
A = np.array([[6, 1], [-2, 3]])

# Calculate and print the eigenvalues
eigenvalues = np.linalg.eigvals(A)
print(f"The eigenvalues are: {eigenvalues}")

