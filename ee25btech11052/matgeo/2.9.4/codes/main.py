import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libvectorcheck.so")

# Define argument/return types
lib.solve_vector.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_vector.restype = ctypes.c_int
lib.verify_solution.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.verify_solution.restype = ctypes.c_int
lib.magnitude.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.magnitude.restype = ctypes.c_double

# Create array for result
b = (ctypes.c_double * 3)()

# Solve for vector b
lib.solve_vector(b)

# Get magnitude
mag = lib.magnitude(b)

# Verify solution
is_correct = lib.verify_solution(b)

print(f"Vector b: ({b[0]}, {b[1]}, {b[2]})")
print(f"Magnitude |b|: {mag}")
print(f"Verification: {'PASS' if is_correct else 'FAIL'}")