import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libmat2.so")

# Define function prototypes
Nd = np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
lib.mat2_square.argtypes = [Nd, Nd]
lib.mat2_square.restype  = None

# Define matrix A (flattened row-major)
A = np.array([1.0, -1.0,
              -1.0,  1.0], dtype=np.double)

A2 = np.empty(4, dtype=np.double)

# Call C function: A2 = A^2
lib.mat2_square(A, A2)

# Reshape for printing
A_mat  = A.reshape(2, 2)
A2_mat = A2.reshape(2, 2)

print("A =\n", A_mat)
print("\nA^2 (from C) =\n", A2_mat)

