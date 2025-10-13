import ctypes
import numpy as np
import sympy as sp

# Load compiled C shared library
lib = ctypes.CDLL("./libgauss.so")

# Define argument types
lib.gauss_solve.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS")
]

def solve_2x2(A, b):
    A_flat = A.astype(np.float64).ravel()
    b_vec = b.astype(np.float64)
    x = np.zeros(2, dtype=np.float64)

    lib.gauss_solve(A_flat, b_vec, x)
    return x

# Example usage
if __name__ == "__main__":
    A = np.array([[4,-3],[3,4]], dtype=np.float64)
    b = np.array([5,0], dtype=np.float64)

    x = solve_2x2(A, b)
    transform_matrix=sp.Matrix([[x[0],-x[1]],[x[1],x[0]]])
    print("Transformation matrix:")
    sp.pprint(transform_matrix)


