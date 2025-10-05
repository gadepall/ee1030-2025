import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
get_parabola_data = lib.get_parabola_data
get_parabola_data.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
get_parabola_data.restype = None

def get_data():
    vertex = np.zeros(2, dtype=np.float64)
    p = ctypes.c_double()
    directrix_x = ctypes.c_double()
    get_parabola_data(vertex, ctypes.byref(p), ctypes.byref(directrix_x))
    return vertex, p.value, directrix_x.value

