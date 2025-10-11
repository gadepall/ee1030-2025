import numpy as np
import ctypes

inverse = ctypes.CDLL('./inverse.so')
inverse.function.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
inverse.function.restype = None

D1 = np.array([1, 0, 0], dtype=np.float64)
D2 = np.array([3, 3, 0], dtype=np.float64)
D3 = np.array([5, 2, 1], dtype=np.float64)

A = np.block([[D1], [D2], [D3]])
v = np.zeros(3, dtype=np.float64)
B = np.block([[v], [v], [v]])
n = 3

inverse.function(
    n,
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

print('The inverted matrix is: ')
print(B)
