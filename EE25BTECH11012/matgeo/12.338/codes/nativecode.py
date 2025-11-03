import numpy as np

# --- Example 1: A real symmetric matrix that IS invertible ---
matrix_A = np.array([
    [3, 1],
    [1, 2]
])

print("## Matrix A ##")
print(matrix_A)

# Check for symmetry: A == A.transpose()
is_symmetric_A = np.all(matrix_A == matrix_A.T)
print(f"Is symmetric? {is_symmetric_A}")

# Check for invertibility by calculating the determinant
det_A = np.linalg.det(matrix_A)
print(f"Determinant: {det_A:.2f}")
print(f"Is invertible? {det_A != 0}")

print("-" * 20)

# --- Example 2: A real symmetric matrix that is NOT invertible ---
matrix_B = np.array([
    [2, 4],
    [4, 8]
])

print("## Matrix B ##")
print(matrix_B)

# Check for symmetry
is_symmetric_B = np.all(matrix_B == matrix_B.T)
print(f"Is symmetric? {is_symmetric_B}")

# Check for invertibility
det_B = np.linalg.det(matrix_B)
print(f"Determinant: {det_B:.2f}")
print(f"Is invertible? {det_B != 0}")