import ctypes
import platform

# Load shared library
if platform.system() == "Windows":
    quad_lib = ctypes.CDLL("./parallelogram.dll")
else:
    quad_lib = ctypes.CDLL("./parallelogram.so")

# Declare function argument & return types
quad_lib.check_quad.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double, ctypes.c_double]
quad_lib.check_quad.restype = ctypes.c_int

# Points: A(1,2,3), B(-1,-2,-1), C(2,3,2), D(4,7,6)
x1,y1,z1 = 1, 2, 3
x2,y2,z2 = -1, -2, -1
x3,y3,z3 = 2, 3, 2
x4,y4,z4 = 4, 7, 6

# Call C function
result = quad_lib.check_quad(x1,y1,z1, x2,y2,z2, x3,y3,z3, x4,y4,z4)

# Interpret result
if result == 0:
    print("ABCD is not a parallelogram.")
elif result == 1:
    print("ABCD is a parallelogram but not a rectangle.")
elif result == 2:
    print("ABCD is a rectangle.")
