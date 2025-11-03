import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./code.so")

# Define function signature: void solve_plane(double *out)
lib.solve_plane.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_plane.restype = None

# Prepare output array
out = (ctypes.c_double * 3)()
lib.solve_plane(out)

# Convert to numpy for convenience
normal_vec = np.array([out[i] for i in range(3)])
print("Normal vector:", normal_vec)


