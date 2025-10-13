import ctypes
import numpy as np

# Load the shared library
matlib = ctypes.CDLL('./libmatfun.so')  # Replace name/path as needed

# Function prototypes
matlib.createMat.argtypes = [ctypes.c_int, ctypes.c_int]
matlib.createMat.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

matlib.solve2x2.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), 
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

matlib.freeMat.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int]

# Example system from image
A = np.array([[7, 2], [4, -7]], dtype=np.float64)
b = np.array([11, 2], dtype=np.float64)
x = np.zeros(2, dtype=np.float64)

# Allocate C matrices
A_ptr = (ctypes.POINTER(ctypes.c_double) * 2)()
for i in range(2):
    row = (ctypes.c_double * 2)()
    row[0], row[1] = A[i, 0], A[i, 1]
    A_ptr[i] = ctypes.cast(row, ctypes.POINTER(ctypes.c_double))

b_ptr = (ctypes.c_double * 2)(*b)
x_ptr = (ctypes.c_double * 2)()

# Solve using C code
matlib.solve2x2(A_ptr, b_ptr, x_ptr)

sol = np.array([x_ptr[0], x_ptr[1]])
print("Solution: x =", sol[0], ", y =", sol[1])

# Free matrix
matlib.freeMat(A_ptr, 2)
