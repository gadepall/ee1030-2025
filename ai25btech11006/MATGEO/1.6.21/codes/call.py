import ctypes

# Load shared library
lib = ctypes.CDLL("./libfunc.so")

lib.check_collinear.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.check_collinear.restype = ctypes.c_int

a, b, c = 1, 2, 3   # change values here

result = lib.check_collinear(a, b, c)

if result == 1:
    print("The points are collinear.")
else:
    print("The points are not collinear.")

