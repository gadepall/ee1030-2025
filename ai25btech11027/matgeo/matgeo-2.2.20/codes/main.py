from ctypes import CDLL, c_double, POINTER

lib = CDLL("./main.so")
lib.angle_between.restype = c_double
lib.angle_between.argtypes = [POINTER(c_double), POINTER(c_double)]

import numpy as np
A = np.array([3.0, 3.0, 4.0], dtype=np.double)   # B - A
B = np.array([6.0, 6.0, 8.0], dtype=np.double)   # D - C

angle = lib.angle_between(A.ctypes.data_as(POINTER(c_double)),
                          B.ctypes.data_as(POINTER(c_double)))
print("Angle =", angle, "degrees")
