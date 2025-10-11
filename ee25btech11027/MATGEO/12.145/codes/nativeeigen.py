import math

def find_eigenvalues_2x2_native(matrix):
    """
    Calculates eigenvalues of a 2x2 matrix using the characteristic polynomial.
    Expects a 2x2 list of lists or NumPy array.
    """
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    # Characteristic equation: lambda^2 - trace*lambda + det = 0
    trace = a + d
    determinant = a * d - b * c

    # Using the quadratic formula
    discriminant = trace**2 - 4 * determinant
    
    # The eigenvalues
    lambda1 = (trace + math.sqrt(discriminant)) / 2
    lambda2 = (trace - math.sqrt(discriminant)) / 2
    
    return lambda1, lambda2

# --- Main part of the script ---
A = [[0, 1],
     [1, 0]]

eig1, eig2 = find_eigenvalues_2x2_native(A)

print(f"Matrix:\n{A[0]}\n{A[1]}\n")
print(f"Eigenvalues from native Python: {eig1} and {eig2}")

# A more 'Pythonic' way using NumPy for verification
import numpy as np

A_np = np.array(A)
numpy_eigenvalues = np.linalg.eigvals(A_np)
print(f"\nFor verification, eigenvalues using NumPy's built-in function: {numpy_eigenvalues}")
