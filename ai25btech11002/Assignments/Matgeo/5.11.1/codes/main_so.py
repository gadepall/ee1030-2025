import numpy as np
import ctypes

# Load the shared library
rank = ctypes.CDLL('./rank.so')
rank.rank.argtypes = [ctypes.c_int, ctypes.c_int, np.ctypeslib.ndpointer(dtype=ctypes.c_double, flags="C_CONTIGUOUS")]
rank.rank.restype = ctypes.c_int

# Augmented matrix for the mesh equations:
# 71I1 - 41I2 = 45
# -41I1 + 62I2 = 35
A = np.array([
    [71, -41, 45],
    [-41, 62, 35]
], dtype=np.float64)

m, n = A.shape
c_matrix = np.ascontiguousarray(A, dtype=ctypes.c_double)

# Call the C function
rank = rank.rank(m, n, c_matrix)

print(f"\nRank of the matrix: {rank}")

