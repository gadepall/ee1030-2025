import ctypes
import numpy as np
import sympy as sp

# Load C library
lib = ctypes.CDLL("./libinverse.so")

# Define function signature
lib.inverse.argtypes = [ctypes.POINTER((ctypes.c_double * 2) * 2),
                        ctypes.POINTER((ctypes.c_double * 2) * 2)]

# Input matrix
A = np.array([[2, -6],
              [1, -2]], dtype=np.double)

inv = np.zeros((2,2), dtype=np.double)

# Call C function
lib.inverse(A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)),
            inv.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 2) * 2)))

inverse=sp.Matrix(inv)
sp.pprint(inverse)

