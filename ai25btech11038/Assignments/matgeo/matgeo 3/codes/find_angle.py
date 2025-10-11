import ctypes
import numpy as np

# Load the .so file
lib = ctypes.CDLL('./dotproduct.so')

# Define argument and return types
lib.dotproduct.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.dotproduct.restype = ctypes.c_double

lib.norm.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.norm.restype = ctypes.c_double

lib.cosine.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.cosine.restype = ctypes.c_double

# Example data
n1 = np.array([1, -1, 0], dtype=np.double)
n2 = np.array([0, 1, -1], dtype=np.double)

# Convert numpy arrays to C pointers
n1_ptr = n1.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
n2_ptr = n2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call functions
dp = lib.dotproduct(n1_ptr, n2_ptr)
norm1 = lib.norm(n1_ptr)
norm2 = lib.norm(n2_ptr)
cos = lib.cosine(dp, norm1, norm2)

print("Dot product:", dp)
print("Norm1:", norm1)
print("Norm2:", norm2)
print("Cosine similarity:", cos)
