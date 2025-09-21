import ctypes

# Load the shared C library
lib = ctypes.CDLL("./libmatrix_solver.so")
lib.det3x3.argtypes = [ctypes.c_double]
lib.det3x3.restype = ctypes.c_double

# Real solution directly
a = -1.0
det_val = lib.det3x3(a)
tol = 1e-6

if abs(det_val) < tol:
    solutions = [a]
else:
    solutions = []

print("Real values of a for infinite solutions:")
print(solutions)

