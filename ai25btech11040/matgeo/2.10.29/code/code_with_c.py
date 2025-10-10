import numpy as np
from ctypes import *

a = np.array([2, -2, 0])
b = np.array([1, 1, -1])
c = np.array([3, 0, -1])

lib = CDLL("./code.so")
lib.volume.argtypes = [c_double] * 9

lib.volume.restype = c_double

volume = lib.volume(a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2])

print(f"Volume of the parallelopiped is {volume}")