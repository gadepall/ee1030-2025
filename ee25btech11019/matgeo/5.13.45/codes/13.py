import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./matrix_ops.so')

# Define argument and return types
lib.determinant3x3.argtypes = [ctypes.c_double * 9]
lib.determinant3x3.restype = ctypes.c_double

lib.inverse3x3.argtypes = [
    (ctypes.c_double * 3 * 3),
    (ctypes.c_double * 3 * 3)
]

lib.multiply3x3.argtypes = [
    (ctypes.c_double * 3 * 3),
    (ctypes.c_double * 3 * 3),
    (ctypes.c_double * 3 * 3)
]

lib.computeR.argtypes = [
    (ctypes.c_double * 3 * 3),
    (ctypes.c_double * 3 * 3),
    (ctypes.c_double * 3 * 3)
]

# Helper to convert NumPy array to ctypes
def to_c_matrix(arr):
    c_matrix = (ctypes.c_double * 3 * 3)()
    for i in range(3):
        for j in range(3):
            c_matrix[i][j] = arr[i, j]
    return c_matrix

def from_c_matrix(c_matrix):
    np_mat = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            np_mat[i,j] = c_matrix[i][j]
    return np_mat

# Input x value
x = 1.0  # you can change this for other checks

# Define matrices
P = np.array([[1,1,1],
              [0,2,2],
              [0,0,3]], dtype=float)

Q = np.array([[2,x,x],
              [0,4,0],
              [x,x,5]], dtype=float)

# Prepare containers for result
R = np.zeros((3,3))

# Convert to C format
cP = to_c_matrix(P)
cQ = to_c_matrix(Q)
cR = to_c_matrix(R)

# Call computeR
lib.computeR(cP, cQ, cR)

# Convert back to NumPy
R = from_c_matrix(cR)

print("Matrix R =")
print(np.round(R, 3))

# Determinant of R (should equal determinant of Q)
detR = np.linalg.det(R)
print(f"\nDeterminant of R = {detR:.3f}")
