import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
get_circle_data = lib.get_circle_data
get_circle_data.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    ctypes.POINTER(ctypes.c_double),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
get_circle_data.restype = None

def get_data():
    c1 = np.zeros(2, dtype=np.float64)
    r1 = ctypes.c_double()
    c2 = np.zeros(2, dtype=np.float64)
    r2 = ctypes.c_double()
    chord_y = ctypes.c_double()

    get_circle_data(c1, ctypes.byref(r1), c2, ctypes.byref(r2), ctypes.byref(chord_y))
    return c1, r1.value, c2, r2.value, chord_y.value

