import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libac.so")   # or "ac.dll" on Windows

# Define argument and return types
lib.compute_AC.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_int
]

# Example: a = [1,0], b = [0,1]
a = np.array([1.0, 0.0], dtype=np.double)
b = np.array([0.0, 1.0], dtype=np.double)
result = np.zeros_like(a)

# Call C function
lib.compute_AC(a, b, result, len(a))

print("Vector AC =", result)

