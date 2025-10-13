import ctypes
import numpy as np

# Load the compiled shared library
lib = ctypes.CDLL('./libmatrixfunc.so')

# Prepare the function prototype for ctypes
lib.mat_power_formula.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int,
                                  np.ctypeslib.ndpointer(dtype=np.float64, shape=(4,))]
lib.mat_power_formula.restype = None

def mat_power_formula(a, b, n):
    result = np.zeros(4, dtype=np.float64)
    lib.mat_power_formula(a, b, n, result)
    return result.reshape((2,2))

# Example usage
a = 2
b = 3
n = 4
matrix = mat_power_formula(a, b, n)
print("Computed (aI + bA)^n:\n", matrix)
