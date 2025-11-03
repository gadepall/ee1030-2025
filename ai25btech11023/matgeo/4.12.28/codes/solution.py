import ctypes
import numpy as np
import os

# Assume matfun.so is compiled from your C code
lib = ctypes.CDLL(os.path.abspath('matfun.so'))

# Define ctypes prototypes from matfun.h (example for dot product and matrix creation)
# double *createMat(int m, int n)
lib.createMat.restype = ctypes.POINTER(ctypes.c_double)
lib.createMat.argtypes = [ctypes.c_int, ctypes.c_int]

# double Matdot(double *a, double *b, int m)
lib.Matdot.restype = ctypes.c_double
lib.Matdot.argtypes = [ctypes.POINTER(ctypes.c_double),
                       ctypes.POINTER(ctypes.c_double),
                       ctypes.c_int]

# Example: Create normal vector and axis direction and check conditions
def get_lambda_case(case):
    if case == "parallel_Y":
        # normal = (2+6λ, 3-λ); n^T e2 = 0 => second component = 0
        # 3 - λ = 0  -> λ = 3
        return 3
    elif case == "perpendicular":
        # Perpendicular to (7, 1): n^T (7, 1) = 0
        # (2+6λ)*7 + (3-λ)*1 = 0 -> 14 + 42λ + 3 - λ = 0 -> 41λ = -17 -> λ = -17/41
        return -17/41
    elif case == "through_P":
        # n^T (1,2) = c = -4 - 12λ
        # (2+6λ)*1 + (3-λ)*2 = -4 - 12λ
        # 2 + 6λ + 6 - 2λ = -4 - 12λ  -> 8 + 4λ = -4 - 12λ -> 16λ = -12 -> λ = -3/4
        return -3/4
    elif case == "parallel_X":
        # n^T e1 = 0 => first component = 0
        # 2 + 6λ = 0 -> λ = -1/3
        return -1/3

print("Case 1: Parallel to Y axis, λ =", get_lambda_case("parallel_Y"))
print("Case 2: Perpendicular, λ =", get_lambda_case("perpendicular"))
print("Case 3: Passes through (1,2), λ =", get_lambda_case("through_P"))
print("Case 4: Parallel to X axis, λ =", get_lambda_case("parallel_X"))

# If you want to use C matrix operations for more general vector calculations:
# a = np.array([2+6*lam, 3-lam], dtype=np.double)
# b = np.array([1,0], dtype=np.double)  # For X-axis direction
# a_ctypes = a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
# b_ctypes = b.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
# dot = lib.Matdot(a_ctypes, b_ctypes, 2)
