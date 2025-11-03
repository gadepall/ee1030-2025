import ctypes
import numpy as np
import sympy as sp

# Load C library
lib = ctypes.CDLL("./5.4.36.so")

# Define function signature
lib.inverse.argtypes = [ctypes.POINTER((ctypes.c_double * 3) * 3),
                        ctypes.POINTER((ctypes.c_double * 3) * 3)]

# Input matrix
A = np.array([[2, -1, -2],
              [0, 2, -1],
              [3, -5, 0]], dtype=np.double)

inv = np.zeros((3,3), dtype=np.double)

# Call C function
lib.inverse(A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 3) * 3)),
            inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 3) * 3)))

inverse=sp.Matrix(inv)
sp.pprint(inverse)
