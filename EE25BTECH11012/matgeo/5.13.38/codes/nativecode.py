import numpy as np

# --- 1. Define Helper Functions ---
def is_skew_symmetric(matrix):
    """
    Checks if a matrix M is skew-symmetric by verifying if M^T = -M.
    Uses np.allclose for accurate floating-point comparisons.
    """
    return np.allclose(matrix.T, -matrix)

def is_symmetric(matrix):
    """Checks if a matrix M is symmetric by verifying if M^T = M."""
    return np.allclose(matrix.T, matrix)

# --- 2. Generate Arbitrary Non-Zero Matrices ---
# To create a skew-symmetric matrix, we can use the formula A - A^T
# To create a symmetric matrix, we can use the formula A + A^T

# Create a random 3x3 matrix to generate X
A = np.random.rand(3, 3)
X = A - A.T  # X is now skew-symmetric

# Create another random 3x3 matrix to generate Y
B = np.random.rand(3, 3)
Y = B - B.T  # Y is now skew-symmetric

# Create a random 3x3 matrix to generate Z
C = np.random.rand(3, 3)
Z = C + C.T  # Z is now symmetric

# --- 3. Verify Properties of Generated Matrices ---
print("--- Initial Matrix Properties ---")
print(f"Is X skew-symmetric? {is_skew_symmetric(X)}")
print(f"Is Y skew-symmetric? {is_skew_symmetric(Y)}")
print(f"Is Z symmetric?      {is_symmetric(Z)}")
print("-" * 35)


# --- 4. Evaluate Each Option ---
print("\n--- Evaluating Each Option ---")

# a) Y^3 * Z^4 - Z^4 * Y^3
# Note: @ is the operator for matrix multiplication in NumPy
M_a = np.linalg.matrix_power(Y, 3) @ np.linalg.matrix_power(Z, 4) - \
      np.linalg.matrix_power(Z, 4) @ np.linalg.matrix_power(Y, 3)
print(f"a) Is Y³Z⁴ - Z⁴Y³ skew-symmetric?  {is_skew_symmetric(M_a)}")

# b) X^44 + Y^44
M_b = np.linalg.matrix_power(X, 44) + np.linalg.matrix_power(Y, 44)
print(f"b) Is X⁴⁴ + Y⁴⁴ skew-symmetric?      {is_skew_symmetric(M_b)}")

# c) X^4 * Z^3 - Z^3 * X^4
M_c = np.linalg.matrix_power(X, 4) @ np.linalg.matrix_power(Z, 3) - \
      np.linalg.matrix_power(Z, 3) @ np.linalg.matrix_power(X, 4)
print(f"c) Is X⁴Z³ - Z³X⁴ skew-symmetric?  {is_skew_symmetric(M_c)}")

# d) X^23 + Y^23
M_d = np.linalg.matrix_power(X, 23) + np.linalg.matrix_power(Y, 23)
print(f"d) Is X²³ + Y²³ skew-symmetric?      {is_skew_symmetric(M_d)}")
print("-" * 35)

