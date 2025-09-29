import ctypes
import sympy as sp

lib = ctypes.CDLL("./problem.so")

lib.get_item.argtypes = [ctypes.c_int, ctypes.c_int]
lib.get_item.restype = ctypes.c_double

lib.get_constant.argtypes = [ctypes.c_int, ctypes.c_int]
lib.get_constant.restype = ctypes.c_double

A = sp.Matrix([[0, 0, 0],
               [0, 0, 0]])


B = sp.Matrix([[0, 0],
               [0, 0]])

for i in range(0,2):
    for j in range(0,2):
        A[i, j] = lib.get_item(i, j)
        B[i, j] = lib.get_item(i, j)


A[0, 2] = lib.get_constant(0, 0)
A[1, 2] = lib.get_constant(1, 0)



rA = A.rank()
rB = B.rank()
n = 2

if rA==rB and rB==n:
    print("Unique solution exist for the given system of linear equations.")
    rref_matrix, pivots = A.rref()
    print("The solution for the given system of linear equations is: x=", rref_matrix[0,2],", y=",rref_matrix[1,2])


elif rA==rB and rA!=n:
    print('Infinite solutions exist for the given system of linear equations in 2 variables.')



else:
    print("No solution exists for the given system of linear equations in 2 variables")

