import ctypes
import numpy as np

lib = ctypes.CDLL("./libmatinv.so")

lib.inverse2x2.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # input matrix
    ctypes.POINTER(ctypes.c_double)   # output matrix
]
lib.inverse2x2.restype = ctypes.c_int

A = np.array([2.0, 1.0, 7.0, 4.0], dtype=np.double)
invA = np.zeros(4, dtype=np.double)

res = lib.inverse2x2(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    invA.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

if res == 0:
    print("Inverse Matrix:")
    print(invA.reshape(2,2))
else:
    print("Matrix is not invertible")

