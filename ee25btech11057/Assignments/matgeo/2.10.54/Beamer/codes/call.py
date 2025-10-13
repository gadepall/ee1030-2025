import ctypes
import math

# Load shared library
lib = ctypes.CDLL("./libcross.so")

# Define function signature
lib.compute_crosses.argtypes = [
    ctypes.POINTER(ctypes.c_double),   # a
    ctypes.POINTER(ctypes.c_double),   # b
    ctypes.POINTER(ctypes.c_double),   # c
    ctypes.POINTER((ctypes.c_double*3)*3)  # result[3][3]
]

# Define the vectors (unit vectors, 120° apart in xy-plane)
a = (ctypes.c_double * 3)(1.0, 0.0, 0.0)
b = (ctypes.c_double * 3)(-0.5, math.sqrt(3)/2, 0.0)
c = (ctypes.c_double * 3)(-0.5, -math.sqrt(3)/2, 0.0)

# Prepare result storage (3x3 array of doubles)
ResultArray = (ctypes.c_double * 3) * 3
result = ResultArray()

# Call the C function
lib.compute_crosses(a, b, c, result)

# Print results
print("a × b =", [result[0][i] for i in range(3)])
print("b × c =", [result[1][i] for i in range(3)])
print("c × a =", [result[2][i] for i in range(3)])

