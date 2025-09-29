import ctypes
import numpy as np


lib = ctypes.CDLL("./libmagnitude.so")


lib.find_magnitude.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C"),
                               ctypes.POINTER(ctypes.c_double)]
lib.find_magnitude.restype = None


x = np.zeros(2, dtype=np.float64)
x_norm = ctypes.c_double()


lib.find_magnitude(x, ctypes.byref(x_norm))


print("Result from C:")
print("x =", x)
print("||x|| =", x_norm.value)


p = np.array([1.0, 0.0])
lhs = np.dot(x - p, x + p)

print("\nVerification in Python:")
print("(x - p)^T (x + p) =", lhs)
print("||x|| =", np.linalg.norm(x))
