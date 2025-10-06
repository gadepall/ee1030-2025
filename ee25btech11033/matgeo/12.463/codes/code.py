import numpy as np
import ctypes
import os

poly_lib = ctypes.CDLL('./code.so')

# Get a handle to the 'p' function from the library
c_poly_func = poly_lib.p
# Specify the argument type (a double)
c_poly_func.argtypes = [ctypes.c_double]
# Specify the return type (a double)
c_poly_func.restype = ctypes.c_double

# The eigenvalues of matrix A are given
eigenvalues_A = np.array([1, -1, 3], dtype=np.double)
print(f"The given eigenvalues of matrix A are: {eigenvalues_A}")



eigenvalues_new_matrix = np.array([c_poly_func(val) for val in eigenvalues_A])
print(f"The calculated eigenvalues using the C function are: {eigenvalues_new_matrix}")

# The trace of a matrix is the sum of its eigenvalues
trace_via_eigenvalues = np.sum(eigenvalues_new_matrix)
print(f"The trace is the sum of these new eigenvalues, which is: {int(trace_via_eigenvalues)}")



