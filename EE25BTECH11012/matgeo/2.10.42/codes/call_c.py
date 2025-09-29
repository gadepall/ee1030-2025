import ctypes

lib = ctypes.CDLL("./libscalartp.so")

lib.computeX_py.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.computeX_py.restype = ctypes.c_double

a = (1.0, 0.0, 0.0)
b = (0.0, 1.0, 0.0)
c = (0.6,0.8,0)

X = lib.computeX_py(*a, *b, *c)
print("X =", X)