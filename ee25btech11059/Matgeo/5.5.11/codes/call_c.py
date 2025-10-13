import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL('./code.so')

# Prepare arguments
A = np.array([[2, 0, -1],
              [5, 1, 0],
              [0, 1, 3]], dtype=np.float64)
A_inv = np.zeros((3, 3), dtype=np.float64)

# Set up argtypes for the C function
lib.invert_matrix.argtypes = [ctypes.POINTER(ctypes.c_double * 3 * 3), ctypes.POINTER(ctypes.c_double * 3 * 3)]

# Create ctypes pointers
A_ct = (ctypes.c_double * 3 * 3)(*A.flatten())
A_inv_ct = (ctypes.c_double * 3 * 3)()

# Call C function
lib.invert_matrix(ctypes.byref(A_ct), ctypes.byref(A_inv_ct))

# Convert result back to numpy
A_inv_result = np.array(A_inv_ct).reshape((3, 3))
print("Inverse matrix from C:\n", A_inv_result)



