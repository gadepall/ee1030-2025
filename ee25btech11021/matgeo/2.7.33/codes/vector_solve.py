import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./cross.so")
lib.find_p.restype = ctypes.c_double

# Call C function
p = lib.find_p()
print("Computed value of p:", p)

# Verify using numpy
A = np.array([2, 6, 27])
B = np.array([1, 3, p])
cross_prod = np.cross(A, B)

print("Cross product A × B =", cross_prod)

if np.allclose(cross_prod, [0, 0, 0]):
    print("✅ A and B are parallel. Solution verified.")
else:
    print("❌ Something went wrong.")

