import ctypes
import numpy as np

lib = ctypes.CDLL('./inv.so')

lib.inverse.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.c_int]
lib.inverse.restype = None


A = np.array([[2, 3],
              [1, 4]], dtype=np.float64)
n = A.shape[0]

A_inv = np.zeros((n, n), dtype=np.float64)

lib.inverse(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            A_inv.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            n)

print("Original matrix:")
print(A)
print("Inverse matrix:")
print(A_inv)
