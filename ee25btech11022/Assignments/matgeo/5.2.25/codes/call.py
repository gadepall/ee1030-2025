import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')

# Function signatures
lib.solve_system.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.generate_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                               np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
                               np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),
                               ctypes.c_int]

def solve_system(a, b, c):
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.solve_system(a, b, c, ctypes.byref(x), ctypes.byref(y))
    return x.value, y.value

def extract_points(a, b, c, n=20):
    xs = np.zeros(n, dtype=np.float64)
    ys = np.zeros(n, dtype=np.float64)
    lib.generate_points(a, b, c, xs, ys, n)
    return xs, ys

if __name__ == "__main__":
    a, b, c = 2, 1, 5
    xsol, ysol = solve_system(a, b, c)
    print("x =", xsol, "; y =", ysol)
    xs, ys = extract_points(a, b, c, 10)
    print("xs:", xs)
    print("ys:", ys)

