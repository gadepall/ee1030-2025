import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("/home/shriyasnh/Desktop/matgeonew/5.5.5/codes/libmatrixcheck.so")

# Define argument/return types
lib.check_matrices.argtypes = [((ctypes.c_double*3)*3), ((ctypes.c_double*3)*3)]
lib.check_matrices.restype = ctypes.c_int

# Define matrices A and B
A = np.array([[1, -1, 0],
              [2,  3, 4],
              [0,  1, 2]], dtype=np.double)

B = np.array([[ 2,  2, -4],
              [-4,  2, -4],
              [ 2, -1,  5]], dtype=np.double)

# Convert numpy arrays to C types
A_c = ((ctypes.c_double*3)*3)(*map(lambda row: (ctypes.c_double*3)(*row), A))
B_c = ((ctypes.c_double*3)*3)(*map(lambda row: (ctypes.c_double*3)(*row), B))

# Call C function
res = lib.check_matrices(A_c, B_c)

print("Correct option is:", res)
