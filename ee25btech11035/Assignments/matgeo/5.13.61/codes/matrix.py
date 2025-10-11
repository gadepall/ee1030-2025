import ctypes
import os

# Load the shared library
lib = ctypes.CDLL(os.path.join(os.getcwd(), "mat.so"))

# Define matrix size
N = 3

# Define argument and return types
lib.getRatio.argtypes = [ctypes.c_double * (N * N), ctypes.c_int]
lib.getRatio.restype = ctypes.c_double

# Prepare matrix P (flattened row-major)
P = [
    1, 0, 0,
    4, 1, 0,
    16, 4, 1
]
P_array = (ctypes.c_double * (N * N))(*P)

# Call the C function
result = lib.getRatio(P_array, 50)
print("Result:", result)
