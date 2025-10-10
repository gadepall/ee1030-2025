import numpy as np
from ctypes import *

p = np.array([7, -6])
q = np.array([3, 4])

lib = CDLL('./code.so')
lib.dividing_point.argtypes = [c_double] * 6

lib.dividing_point.restype = c_int

l = 1
m = 2

quadrant = lib.dividing_point(p[0], q[0], p[1], q[1], l, m)
print(f"Q{quadrant}")