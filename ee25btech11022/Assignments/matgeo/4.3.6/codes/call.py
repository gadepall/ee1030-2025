import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')

def get_points_and_line():
    A = np.zeros(3, dtype=np.float64)
    B = np.zeros(3, dtype=np.float64)
    n = np.zeros(3, dtype=np.float64)
    k = ctypes.c_double()
    lib.get_points_and_line.argtypes = [
        ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
    ]
    lib.get_points_and_line(
        A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        n.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        ctypes.byref(k)
    )
    return A, B, n, k.value

if __name__ == "__main__":
    A, B, n, k = get_points_and_line()
    print("Point A:", A)
    print("Point B:", B)
    print("Normal Vector n:", n)
    print("Constant k:", k)

