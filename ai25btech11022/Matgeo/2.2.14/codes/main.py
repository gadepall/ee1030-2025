import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./liblineplane.so")

# Define argument and return types for the C function
lib.angle_line_plane.argtypes = [ctypes.c_double * 3, ctypes.c_double * 3]
lib.angle_line_plane.restype = ctypes.c_double

# Define vectors (line direction, plane normal)
d = (ctypes.c_double * 3)(2, -1, 1)
n = (ctypes.c_double * 3)(3, -4, -1)

# Call C function
theta = lib.angle_line_plane(d, n)

print("Angle between line and plane (from C) = {:.6f} degrees".format(theta))

