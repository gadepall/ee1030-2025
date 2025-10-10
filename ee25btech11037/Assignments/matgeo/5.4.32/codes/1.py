import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./mat.so")

# Define argument types: one 3x3 float matrix
lib.inverse.argtypes = [(ctypes.c_float * 3) * 3]
lib.inverse.restype = None

# Define a matrix in numpy
A = np.array([
    [1, 0, 1],
    [0, 1, 2],
    [0, 0, 4]
], dtype=np.float32)

# Convert numpy array -> ctypes 2D array
A_ctypes = ((ctypes.c_float * 3) * 3)(*[
    (ctypes.c_float * 3)(*row) for row in A
])

# Call the C function (prints from C)
lib.inverse(A_ctypes)

