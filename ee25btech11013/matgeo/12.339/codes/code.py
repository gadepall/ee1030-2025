import numpy as np
import ctypes

lib = ctypes.CDLL("./libcode.so")  


lib.det.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.det.restype = ctypes.c_double

A = np.array([[3, -3],
              [-3, 4]], dtype=np.float64)

I = np.eye(2, dtype=np.float64)

expr = -A @ A + 7*A - 3*I
mat_flat = expr.flatten()
det_value = lib.det(mat_flat.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print("Matrix (-A^2 + 7A - 3I):\n", expr)
print("Determinant =", det_value)

