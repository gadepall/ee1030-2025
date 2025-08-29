import ctypes
import numpy as np

lib = ctypes.cdll.LoadLibrary('./code.so')

lib.division_point.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)]
lib.division_point.restype = None

def get_points():
    A = np.array([1, -5], dtype=np.double)
    B = np.array([-4, 5], dtype=np.double)
    P = np.zeros(2, dtype=np.double)
    k = ctypes.c_double()
    lib.division_point(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       P.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       ctypes.byref(k))
    return P, k.value, A, B

