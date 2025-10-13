import ctypes
import numpy as np

# load shared object
lib = ctypes.CDLL("./verify.so")

# declare arg + return types
lib.expr_value.argtypes = [ctypes.c_double * 3,
                           ctypes.c_double * 3,
                           ctypes.c_double * 3]
lib.expr_value.restype = ctypes.c_double

def to_c_array(v):
    return (ctypes.c_double * 3)(*v)

# random vectors
a = np.random.randn(3)
b = np.random.randn(3)
c = np.random.randn(3)

# C result
res_c = lib.expr_value(to_c_array(a), to_c_array(b), to_c_array(c))

# Python verification: should be ≈ -det([a,b,c])
res_py = -np.dot(a, np.cross(b, c))

print("C result:", res_c)
print("Python check (-[a b c]):", res_py)
print("Difference:", abs(res_c - res_py))
