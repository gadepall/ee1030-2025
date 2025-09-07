import ctypes
import numpy as np

# Load compiled shared library
lib = ctypes.CDLL("./plane.so")   # use "plane.dll" on Windows

D = 3
IntArray3 = ctypes.c_int * D

# Bind functions
lib.vec_sub.argtypes = [IntArray3, IntArray3, IntArray3]
lib.dot.argtypes = [IntArray3, IntArray3]
lib.dot.restype = ctypes.c_int
lib.scalar_mul.argtypes = [ctypes.c_int, IntArray3, IntArray3]

def vec_sub(U, V):
    U_arr, V_arr, C_arr = IntArray3(*U), IntArray3(*V), IntArray3()
    lib.vec_sub(U_arr, V_arr, C_arr)
    return list(C_arr)

def dot(U, V):
    return lib.dot(IntArray3(*U), IntArray3(*V))

def scalar_mul(k, V):
    V_arr, R_arr = IntArray3(*V), IntArray3()
    lib.scalar_mul(k, V_arr, R_arr)
    return list(R_arr)

if __name__ == "__main__":
    A = [3, 4, -5]
    B = [-2, 1, 4]

    BminusA = vec_sub(B, A)
    left_row = scalar_mul(2, BminusA)
    rhs = dot(B, B) - dot(A, A)

    print("Using C library through ctypes:")
    print("B - A =", BminusA)
    print("Left row vector 2(B - A)^T =", left_row)
    print("RHS scalar =", rhs)
    print(f"Equation of plane: {left_row[0]}x + {left_row[1]}y + {left_row[2]}z = {rhs}")
    