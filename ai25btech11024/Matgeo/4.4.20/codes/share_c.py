import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libline.so")

# Define argument and return types for det
lib.det.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.det.restype = ctypes.c_double

# Define argument and return types for line
lib.line.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_double]
lib.line.restype = ctypes.c_int

# For line: array of 2 doubles and a double
n = (ctypes.c_double * 2)(2.0, -5.0)
a = ctypes.c_double(6.0)

result_line = lib.line(n, a)

if result_line==0 :
    print("lines are intersecting")
elif result_line==1 :
    print("lines are parallel")
else :
    print("lines are colinear")
