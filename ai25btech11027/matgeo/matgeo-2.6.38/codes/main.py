import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL('./main.so')

# Define arg types for compute_vector_c: pointer to double
lib.compute_vector_c.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS')]

# Output array to be filled by C function
c = np.zeros(3, dtype=np.float64)

# Call the C function, passing pointer to array c
lib.compute_vector_c(c)

print("Computed vector c:", c)

# Verification
a = np.array([1, 1, 1])
b = np.array([0, 1, -1])

print("a · c =", np.dot(a, c))
print("a × c =", np.cross(a, c))
print("Expected b =", b)

