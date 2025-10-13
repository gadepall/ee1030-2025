import ctypes
import os
import numpy as np

# Load C library
lib = ctypes.CDLL(os.path.abspath("./matrix_inverse.so"))

# Define function signatures
ArrayType = ctypes.c_float * 9  # 3x3 = 9 elements

lib.matrix_inverse.argtypes = [ArrayType, ArrayType]
lib.matrix_inverse.restype = ctypes.c_int

def c_matrix_inverse(A):
    A = np.array(A, dtype=np.float32).reshape(9)
    A_c = ArrayType(*A)
    inv_c = ArrayType()

    success = lib.matrix_inverse(A_c, inv_c)
    if not success:
        raise ValueError("Matrix is singular, no inverse exists.")

    inv = np.array(list(inv_c), dtype=np.float32).reshape(3, 3)
    return inv

# --- Example ---
A = [
    [1, -1, 2],
    [2,  3, 5],
    [-2, 0, 1]
]

inv = c_matrix_inverse(A)

print("Original matrix A:")
print(np.array(A, dtype=np.float32))

print("\nInverse of A (from C function):")
print(inv)

print("\nCheck with NumPy:")
print(np.linalg.inv(np.array(A, dtype=np.float32)))
