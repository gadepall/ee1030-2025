import ctypes

lib = ctypes.CDLL("./code.so")

lib.positiveeigenvalue.argtypes = [ctypes.c_double, ctypes.c_double,
                                    ctypes.c_double, ctypes.c_double]
lib.positiveeigenvalue.restype = ctypes.c_double
a, b, c, d = 2.0, 1.0, 5.0, 2.0

pos_eig = lib.positiveeigenvalue(a, b, c, d)
print("The positive eigenvalue is:", pos_eig)

