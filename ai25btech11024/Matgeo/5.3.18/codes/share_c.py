import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libeqn.so')

# Prepare argument types
lib.solve.argtypes = [ctypes.POINTER(ctypes.c_double * 3 * 3), ctypes.POINTER(ctypes.c_double * 3)]
lib.solve.restype = None

# Prepare input data as numpy arrays
arr = np.array([[2.0, -3.0, 5.0], [3.0, 2.0, -4.0], [1.0, 1.0, -2.0]], dtype=np.float64)
b = np.array([13.0, -2.0, -2.0], dtype=np.float64)

# Convert to correct ctypes
arr_ctypes = (ctypes.c_double * 3 * 3)()
for i in range(3):
    for j in range(3):
        arr_ctypes[i][j] = arr[i][j]
b_ctypes = (ctypes.c_double * 3)(*b)

# Call the function
lib.solve(ctypes.byref(arr_ctypes), ctypes.byref(b_ctypes))

