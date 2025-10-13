import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libgauss.so')

# Define return type and argument types
lib.gauss_elimination.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.gauss_elimination.restype = None

# Prepare array for results
res = (ctypes.c_double * 3)()

# Call the function
lib.gauss_elimination(res)

# Convert to Python list
solution = [res[i] for i in range(3)]
print("Solution (x, y, z) =", solution)
