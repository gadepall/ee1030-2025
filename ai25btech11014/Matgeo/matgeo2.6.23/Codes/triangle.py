import ctypes
import numpy as np

lib = ctypes.CDLL('./libtriangle.so')
lib.triangle_area.argtypes = [ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)]
lib.triangle_area.restype = ctypes.c_float

U = np.array([0, 1, 2], dtype=np.float32)
V = np.array([1, 2, 0], dtype=np.float32)

area = lib.triangle_area(U.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                         V.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))
print(f"Area = {area}")
