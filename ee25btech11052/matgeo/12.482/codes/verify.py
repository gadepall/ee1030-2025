import numpy as np

# 1. Define the matrix from the document [cite: 6]
M = np.array([[5, 3],
              [3, 5]])

# 2. Calculate eigenvalues and eigenvectors
#    np.linalg.eig returns the eigenvalues and the corresponding
#    normalized eigenvectors (as columns in a matrix).
eigenvalues, eigenvectors = np.linalg.eig(M)

# 3. Find the index of the smallest eigenvalue
min_eigenvalue_index = np.argmin(eigenvalues)

# 4. Get the smallest eigenvalue and its corresponding eigenvector
smallest_eigenvalue = eigenvalues[min_eigenvalue_index]
smallest_eigenvector = eigenvectors[:, min_eigenvalue_index]

# 5. Print the results to verify
print(f"The calculated eigenvalues are: {eigenvalues}")
print(f"The smallest eigenvalue is: {smallest_eigenvalue:.0f}\n") # .0f to show it as an integer

print(f"The normalized eigenvector for the smallest eigenvalue is:")
print(smallest_eigenvector)

# For comparison with the document's answer: 1/sqrt(2) is approx 0.707
