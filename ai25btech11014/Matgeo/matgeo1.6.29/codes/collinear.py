import ctypes
import numpy as np

# Load the shared object
lib = ctypes.CDLL("./libcentroid.so")
lib.centroid.argtypes = [ctypes.POINTER(ctypes.c_double)] * 4

# Define input vectors
A = np.array([3.0, -5.0, 7.0])
B = np.array([-1.0, 7.0, -6.0])
G = np.array([1.0, 1.0, 1.0])
C = np.zeros(3)

# Convert to ctypes pointers
A_ct = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
B_ct = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
G_ct = G.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
C_ct = C.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call the C function
lib.centroid(A_ct, B_ct, G_ct, C_ct)

# Display result
print("Coordinates of C:", C)
