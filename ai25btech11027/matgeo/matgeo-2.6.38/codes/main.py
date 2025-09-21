import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
from scipy.optimize import bisect  # For root-finding

# Load C shared library
lib = ctypes.CDLL('./main.so')

lib.scalar_triple_product.argtypes = [
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")
]
lib.scalar_triple_product.restype = ctypes.c_double

# Given vectors
a = np.array([1.0, 1.0, 1.0], dtype=np.double)
b = np.array([0.0, 1.0, -1.0], dtype=np.double)
c0 = np.array([3.0, 0.0, 0.0], dtype=np.double)
d = np.array([-2.0, 1.0, 1.0], dtype=np.double)

# Define function f(lambda) = scalar triple product - 2
def f(lam):
    c = c0 + lam * d
    val = lib.scalar_triple_product(a, b, c)
    return val - 2.0

# Find lambda root where f(lambda) = 0
# Use interval where lambda is expected (for example between 0 and 2)
lambda_root = bisect(f, 0, 2)

print(f"Found lambda = {lambda_root:.6f}")

# Compute c using found lambda
c_final = c0 + lambda_root * d
print(f"Vector c = {c_final}")

