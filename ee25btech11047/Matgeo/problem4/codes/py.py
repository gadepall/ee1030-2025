import numpy as np
import ctypes
# Local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# Load C math library for sqrt
libm = ctypes.CDLL("libm.so.6")
libm.sqrt.restype = ctypes.c_double
libm.sqrt.argtypes = [ctypes.c_double]

# Given values
a = 4.0        # |a|
lhs = 144.0    # |a × b|^2 + (a · b)^2

# Compute b^2 using NumPy
b_squared = lhs / np.power(a, 2)

# Compute b using C's sqrt via ctypes
b = libm.sqrt(ctypes.c_double(b_squared))

print(f"|b| = {b}")
