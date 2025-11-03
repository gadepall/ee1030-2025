import numpy as np
import ctypes


lib = ctypes.CDLL("./libcode.so")
# Define function argument and return types
lib.matmul_transpose.argtypes = [((ctypes.c_double * 3) * 3), ((ctypes.c_double * 3) * 3)]

# Convert numpy array to C 2D array
def to_c_matrix(A):
    c_mat = ((ctypes.c_double * 3) * 3)()
    for i in range(3):
        for j in range(3):
            c_mat[i][j] = A[i][j]
    return c_mat

# Convert C 2D array back to numpy
def from_c_matrix(c_mat):
    return np.array([[c_mat[i][j] for j in range(3)] for i in range(3)])

# Function to verify example
def verify_matrix(P, name):
    print(f"\n--- {name} ---")
    print("Matrix P:\n", P)

    P_c = to_c_matrix(P)
    result_c = ((ctypes.c_double * 3) * 3)()
    lib.matmul_transpose(P_c, result_c)

    PT_P = from_c_matrix(result_c)
    print("\nP^T * P =\n", PT_P)
    print("\nIs P orthogonal?", np.allclose(PT_P, np.eye(3)))

    eigenvalues, _ = np.linalg.eig(P)
    print("\nEigenvalues of P:", eigenvalues)

# Example 1: λ = 1
P1 = np.array([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]], dtype=float)

# Example 2: λ = -1
P2 = np.array([[-1, 0, 0],
               [0, 1, 0],
               [0, 0, -1]], dtype=float)

verify_matrix(P1, "Example 1 (λ = 1)")
verify_matrix(P2, "Example 2 (λ = -1)")

