import ctypes
import numpy as np

lib = ctypes.CDLL("./libages.so")

lib.solve2x2.argtypes = [
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]
lib.solve2x2.restype = ctypes.c_int

a11, a12, b1 = 1, -3, 10
a21, a22, b2 = 1, -7, -30

sol = (ctypes.c_double * 2)()

res = lib.solve2x2(a11, a12, a21, a22, b1, b2, sol)

if res == 0:
    r, s = sol[0], sol[1]
    print(f"Rahul's age = {r:.0f}, Son's age = {s:.0f}")
else:
    print("No unique solution")

