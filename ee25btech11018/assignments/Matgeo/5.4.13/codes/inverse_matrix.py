import ctypes
import numpy as np
import sympy as sp

# Load the compiled shared library (.so file)
lib = ctypes.CDLL("./inverse_matrix.so")

# Define the argument types for the inverse function
lib.inverse.argtypes = [
    ctypes.POINTER((ctypes.c_double * 2) * 2),
    ctypes.POINTER((ctypes.c_double * 2) * 2)
]

# Define the 2x2 input matrix A
A = np.array([[1, 3],
              [2, 7]], dtype=np.double)

# Prepare an empty matrix for the inverse
inv = np.zeros((2, 2), dtype=np.double)

# Call the C function: inverse(A, inv)
lib.inverse(
    A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)),
    inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2))
)

# Convert the result to a Sympy Matrix for clean display
inverse = sp.Matrix(inv)

print("Inverse of the matrix:")
sp.pprint(inverse)

