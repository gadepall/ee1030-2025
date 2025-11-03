import numpy as np
import ctypes

c_lib = ctypes.CDLL("./code.so")

c_lib.inverse.argtypes = [ctypes.POINTER((ctypes.c_double * 3))]

A = np.array([
    [1.0, -3.0, 2.0],
    [-3.0, 0.0, -5.0],
    [2.0, 5.0, 0.0]
], dtype=np.float64)

B = A.ctypes.data_as(ctypes.POINTER((ctypes.c_double * 3)))

c_lib.inverse(B)

np.set_printoptions(precision=2)

print(A)

