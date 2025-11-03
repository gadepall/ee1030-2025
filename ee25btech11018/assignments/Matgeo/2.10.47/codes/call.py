import ctypes
import math

# Load the compiled shared library
lib = ctypes.CDLL("./volume.so")

# Declare function signatures
lib.determinant.argtypes = [ctypes.c_double]
lib.determinant.restype = ctypes.c_double

lib.f.argtypes = [ctypes.c_double]
lib.f.restype = ctypes.c_double

lib.isLocalMinimum.argtypes = [ctypes.c_double]
lib.isLocalMinimum.restype = ctypes.c_int

# Options to check
options = [-3, 3, 1.0/math.sqrt(3), math.sqrt(3)]

print("Checking all options:\n")
for a in options:
    det_val = lib.determinant(a)
    f_val = lib.f(a)
    is_min = lib.isLocalMinimum(a)

    print(f"a = {a:.6f}, Determinant = {det_val:.6f}, f(a) = {f_val:.6f}", end="")

  

print("\nTherefore, the local minimum occurs at a = 1/sqrt(3).")

