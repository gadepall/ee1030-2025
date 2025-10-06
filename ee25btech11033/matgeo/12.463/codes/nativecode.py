import numpy as np
eigenvalues_A = np.array([1, -1, 3])
print(f"The given eigenvalues of matrix A are: {eigenvalues_A}")

def p(x):
  """Represents the polynomial p(x) = x^3 - 3x^2."""
  return x**3 - 3 * x**2

eigenvalues_new_matrix = p(eigenvalues_A)
print(f"The calculated eigenvalues of the matrix (A^3 - 3A^2) are: {eigenvalues_new_matrix}")

trace_via_eigenvalues = np.sum(eigenvalues_new_matrix)
print(f"The trace is the sum of these new eigenvalues, which is: {trace_via_eigenvalues}")
