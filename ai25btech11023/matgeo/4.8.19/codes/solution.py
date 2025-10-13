import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL('./solution.so')

# Set argument and return types
lib.solve_lambda.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
    ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double)
]
lib.solve_lambda.restype = None

def create_mat_py(values):
    """Create C-compatible double** from Python nested lists."""
    m = len(values)
    n = len(values[0])
    ArrayType = ctypes.POINTER(ctypes.c_double) * m
    mat = ArrayType()
    for i in range(m):
        row = (ctypes.c_double * n)(*values[i])
        mat[i] = row
    return mat

# Prepare inputs
n_values = [[1.0], [-1.0], [1.0]]
P_values = [[1.0], [1.0], [1.0]]
d = 5.0 / np.sqrt(3)

n_c = create_mat_py(n_values)
P_c = create_mat_py(P_values)
lambda_out = (ctypes.c_double * 2)()

# Call C function
lib.solve_lambda(n_c, P_c, ctypes.c_double(d), lambda_out)

print(f"Possible values of lambda: {lambda_out[0]}, {lambda_out[1]}")
