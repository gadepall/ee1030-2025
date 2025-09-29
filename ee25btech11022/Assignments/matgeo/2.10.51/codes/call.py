import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
lib.get_orthogonal_vectors.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

def get_orthogonal_vectors(a, b, c):
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    c = np.array(c, dtype=np.float64)
    out_a = np.zeros(3, dtype=np.float64)
    out_b1 = np.zeros(3, dtype=np.float64)
    out_c3 = np.zeros(3, dtype=np.float64)
    lib.get_orthogonal_vectors(
        a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        out_a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        out_b1.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        out_c3.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    )
    return out_a, out_b1, out_c3



