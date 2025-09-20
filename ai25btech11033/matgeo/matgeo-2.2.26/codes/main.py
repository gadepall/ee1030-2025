import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./main.so')

# Define function signature
lib.angle_between_vectors.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.angle_between_vectors.restype = ctypes.c_double

# Define vectors
a = np.array([1.0, 2.0, 2.0], dtype=np.float64)
b = np.array([3.0, 2.0, 6.0], dtype=np.float64)

# Call the function
angle = lib.angle_between_vectors(a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                                   b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print(f"Angle between vectors: {angle:.2f} degrees")

