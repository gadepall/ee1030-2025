# call.py
import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
get_points = lib.get_points
get_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
                       np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,))]
get_points.restype = None

def get_points_from_c():
    A = np.zeros(2, dtype=np.float64)
    B = np.zeros(2, dtype=np.float64)
    get_points(A, B)
    return A, B

