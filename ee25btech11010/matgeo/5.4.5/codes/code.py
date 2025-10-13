import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./code.so")   

# Define the function signature
lib.inverse2x2.argtypes = [
    (ctypes.c_double * 2) * 2,  # input matrix A
    (ctypes.c_double * 2) * 2   # output matrix inv
]
lib.inverse2x2.restype = ctypes.c_int

# Prepare input matrix
A = ((ctypes.c_double * 2) * 2)()
A[0][0], A[0][1] = 1.0, 2.0
A[1][0], A[1][1] = 2.0, 1.0

# Prepare output matrix
inv = ((ctypes.c_double * 2) * 2)()

# Call the C function
status = lib.inverse2x2(A, inv)

if status:
    # Convert result to numpy array for convenience
    result = np.array([[inv[0][0], inv[0][1]],
                       [inv[1][0], inv[1][1]]])
    print("Inverse matrix:")
    print(result)
else:
    print("Matrix is singular — no inverse.")




