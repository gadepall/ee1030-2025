import ctypes
import numpy as np

lib = ctypes.CDLL("./libmatmul.so")

lib.matmul.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),  # A
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),  # B
    np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS"),  # C
]
lib.matmul.restype = None

A = np.array([[-1, 5],
              [-3, 2]], dtype=np.float64)

B = (1/13.0) * np.array([[2, -5],
                         [3, -1]], dtype=np.float64)

C = np.zeros((2, 2), dtype=np.float64)

lib.matmul(A, B, C)

print("A =\n", A)
print("B =\n", B)
print("C = A*B =\n", C) 
