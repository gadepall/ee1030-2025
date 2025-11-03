import ctypes
import numpy as np

lib = ctypes.CDLL('./libtriangle.so')
lib.solve_triangle.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float)
]

A = np.array([
    [1, 1, 1],
    [-1, 0, -0.2588],
    [0, 1, -0.9659]
], dtype=np.float32)

b = np.array([10, 0, 0], dtype=np.float32)
x = np.zeros(3, dtype=np.float32)

lib.solve_triangle(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    b.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
)

print("Solution [a b c]:", x)

