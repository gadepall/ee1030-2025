import numpy as np

# Define two 3x3 matrices A and B
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

# Compute AB
AB = np.dot(A, B)

# Compute transpose of AB
ABt = AB.T

# Compute B^T * A^T
BtAt = np.dot(B.T, A.T)

# Print results
print("Transpose of AB:")
print(ABt)

print("Product B^T A^T:")
print(BtAt)
