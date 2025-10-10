import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./main.so")

# Define C function signature
IntArray2 = ctypes.c_int * 2
lib.rank_matrix.argtypes = [IntArray2, IntArray2]
lib.rank_matrix.restype = ctypes.c_int

# Points
A = np.array([-5, 1])
C = np.array([4, -2])
x2 = 1

possible_p = []
for p in range(-20, 21):  # check p in [-20,20]
    B = np.array([x2, p])

    row1 = (B - A).astype(int)
    row2 = (C - A).astype(int)

    # Convert numpy arrays to C arrays
    row1_c = IntArray2(row1[0], row1[1])
    row2_c = IntArray2(row2[0], row2[1])

    r = lib.rank_matrix(row1_c, row2_c)
    if r == 1:
        possible_p.append(p)

print("Values of p that make points collinear:", possible_p)
