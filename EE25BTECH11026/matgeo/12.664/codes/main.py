import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libmatrix_ops.so")

N = 10
MAX_ITER = 1000
TOL = 1e-9

# Define argument types
lib.inverse.argtypes = [ctypes.c_int,
                        (ctypes.c_double * N * N),
                        (ctypes.c_double * N * N)]
lib.inverse.restype = ctypes.c_int

lib.qr_iteration.argtypes = [ctypes.c_int,
                             (ctypes.c_double * N * N),
                             (ctypes.c_double * N),
                             ctypes.c_int,
                             ctypes.c_double]


def matrix_inverse(A: np.ndarray):
    n = A.shape[0]
    A_c = (ctypes.c_double * N * N)()
    Inv_c = (ctypes.c_double * N * N)()

    for i in range(n):
        for j in range(n):
            A_c[i][j] = A[i, j]

    success = lib.inverse(n, A_c, Inv_c)
    if not success:
        raise ValueError("Matrix is singular")

    Inv = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            Inv[i, j] = Inv_c[i][j]

    return Inv

# Wrapper: Eigenvalues
def eigenvalues(A: np.ndarray):
    n = A.shape[0]
    A_c = (ctypes.c_double * N * N)()
    eig_c = (ctypes.c_double * N)()

    for i in range(n):
        for j in range(n):
            A_c[i][j] = A[i, j]

    lib.qr_iteration(n, A_c, eig_c, MAX_ITER, TOL)

    return np.round(np.array([eig_c[i] for i in range(n)]), 3)

# Example 
if __name__ == "__main__":
    A = np.array([[4.0, 2.0, 1.0],
                  [1.0, 3.0, 2.0],
                  [0.0, 5.0, 6.0]])
    B=matrix_inverse(A)
    print("Eigenvalues of A:",eigenvalues(A))
    print("Eigenvalues of B:",eigenvalues(B))

