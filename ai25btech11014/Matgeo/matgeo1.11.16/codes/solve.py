import ctypes
import numpy as np
from sympy import Matrix, sqrt

# Load the shared library
lib = ctypes.CDLL('./libdircos.so')
dir_cos = lib.direction_cosines
dir_cos.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

# Prepare input and output arrays
D = np.array([2.0, 2.0, 3.0])
L = np.zeros(3)

# Call the C function
dir_cos(D.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        L.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print("Direction Cosines:", L)
