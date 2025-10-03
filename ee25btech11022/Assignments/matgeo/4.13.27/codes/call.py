import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
lib.generate_points.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
    ctypes.c_int,
    ctypes.c_double
]

def extract_points(n=10, t=2.0):
    x = np.zeros(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    lib.generate_points(x, y, n, t)
    return x, y

if __name__ == "__main__":
    x, y = extract_points(10, 2.0)
    print("x:", x)
    print("y:", y)

