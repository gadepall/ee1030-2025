import ctypes as ct
import sympy as sp

lib = ct.CDLL("./problem.so")
entry = ct.c_double*7
lib.make_data.argtypes = [ct.POINTER(ct.c_double)]
lib.processing.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double, ct.c_double]
data = entry()
lib.make_data(data)
A = sp.Matrix([[data[0], data[1], data[2]],
                   [data[3], data[4], data[5]]])
B = sp.Matrix([[data[0], data[1]],
                   [data[3], data[4]]])
C = ([data[0], data[3]])
D = ([data[1], data[4]])
E = data[2]
F = data[5]
n = data[6]
def get_data():
    return C, D, E, F

rA = A.rank()
rB = B.rank()
rref_matrix, pivots = A.rref()

lib.processing(rA, rB, n, rref_matrix[0,2], rref_matrix[1,2])