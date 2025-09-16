import numpy as np
from ctypes import *

a = np.array([1, -2])

lib = CDLL('./code.so')
lib.vec_x.argtypes = [c_double] * 3
lib.vec_y.argtypes = [c_double] * 3

lib.vec_x.restype = c_double
lib.vec_y.restype = c_double

m = 7

r = np.array([lib.vec_x(a[0], a[1], m), lib.vec_y(a[0], a[1], m)])

print(r)