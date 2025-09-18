import numpy as np

# Define the given matrix A
A = np.array([
    [1, 1, 1],
    [1, 2, -2],
    [2, -1, 3]
])
I = np.eye(3)

# Calculate powers as needed
A2 = np.matmul(A, A)
A3 = np.matmul(A2, A)

# Use Cayley-Hamilton theorem result to compute inverse
# A^{-1} = 1/11 * ( -A^2 + 6A - 5I )
A_inv = ( -A2 + 6*A - 5*I ) / 11

# Print the inverse matrix
print('Inverse of A:')
for row in A_inv:
    print([f'{elem:.4f}' for elem in row])

