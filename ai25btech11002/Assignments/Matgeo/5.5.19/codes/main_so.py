import numpy as np
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libinv.so')

# Define the C function signature
# Use c_double * 3 for each row, and [3] for the 2D array
lib.matrix_inverse.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, shape=(3,3)),
                              np.ctypeslib.ndpointer(dtype=np.float64, shape=(3,3))]
lib.matrix_inverse.restype = None

# Define the 3x3 matrix A
A = np.array([[2, -3, 5],
              [3, 2, -4],
              [1, 1, -2]], dtype=np.float64)

# Create output array for the inverse
inv = np.zeros((3, 3), dtype=np.float64)

# Call the C function
lib.matrix_inverse(A, inv)


