import ctypes
import numpy as np

# Load the shared object file
lib = ctypes.CDLL('./problem.so')

# Set argument types for solve_lambda
lib.solve_lambda.argtypes = [ctypes.POINTER(ctypes.c_double)]

# Set return type
lib.solve_lambda.restype = ctypes.c_double

b = np.array([1.0, 2.0, 3.0], dtype=np.double)

b_ptr = b.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

lambda_val = lib.solve_lambda(b_ptr)
print(f"Solved lambda: {lambda_val}")

