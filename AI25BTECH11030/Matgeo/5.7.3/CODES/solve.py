import ctypes
import numpy as np

SIZE = 3

lib = ctypes.CDLL('./libmatfun.so')

Matrix3x3 = ctypes.c_double * (SIZE*SIZE)

def np_to_c_matrix(np_mat):
    flat = np_mat.flatten()
    return Matrix3x3(*flat)

def c_matrix_to_np(c_mat):
    return np.array(list(c_mat)).reshape((SIZE, SIZE))

# Prototype for compute_inverse
lib.compute_inverse.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Matrix A
A_np = np.array([[1,1,1],
                [1,2,-2],
                [2,-1,3]], dtype=np.double)

A_c = np_to_c_matrix(A_np)
A_inv_c = Matrix3x3()

# Call the C function
lib.compute_inverse(A_c, A_inv_c)

A_inv_np = c_matrix_to_np(A_inv_c)

print("Inverse matrix A^-1:")
for row in A_inv_np:
    print(" ".join(f"{x: .4f}" for x in row))

