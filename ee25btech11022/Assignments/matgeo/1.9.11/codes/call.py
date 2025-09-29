import ctypes
import numpy as np

# Load compiled shared library
lib = ctypes.CDLL('./code.so')

# Set function argument and return types
lib.find_k_and_points.argtypes = [
    ctypes.POINTER(ctypes.c_double),          # double *k
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS'), # pt1[2]
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags='C_CONTIGUOUS')  # pt2[2]
]
lib.find_k_and_points.restype = None

def get_points():
    k = ctypes.c_double()
    pt1 = np.zeros(2, dtype=np.double)
    pt2 = np.zeros(2, dtype=np.double)
    lib.find_k_and_points(ctypes.byref(k), pt1, pt2)
    return k.value, pt1, pt2

