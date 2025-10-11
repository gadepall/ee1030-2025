import ctypes
import sys

# Load shared object (compiled from your C code)
lib = ctypes.CDLL("./condition_no.so")

# Define the C function signature
lib.condition_number.argtypes = [((ctypes.c_double * 2) * 2)]
lib.condition_number.restype = ctypes.c_double

# Define the input matrix A = [[2, 1], [0, 3]]
A = ((ctypes.c_double * 2) * 2)()
A[0][0] = 2.0
A[0][1] = 1.0
A[1][0] = 0.0
A[1][1] = 3.0

# Call the C function
cond_num = lib.condition_number(A)
print(f"Condition number of A: {cond_num}")

