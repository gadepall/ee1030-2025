import numpy as np

# The 'b' variable from your problem
b = 0.0 # You can change this value to test other cases

# Define the matrix from the problem as a NumPy array
# A = [[1+b, b, 1], [b, 1+b, 1], [1, 2b, 1]]
matrix = np.array([
    [1 + b, b, 1],
    [b, 1 + b, 1],
    [1, 2 * b, 1]
], dtype=float)

# Calculate the determinant using NumPy's linalg.det function
determinant_value = np.linalg.det(matrix)

# Print the result
print(f"The matrix (for b={b}):")
print(matrix)
print(f"\nDeterminant calculated using NumPy: {determinant_value}")
