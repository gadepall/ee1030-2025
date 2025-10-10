import ctypes

import numpy as np 

lib = ctypes.CDLL("./libcode.so")

array = ctypes.c_int * 3
matrix = array * 3
lib.determinant.argtypes = [matrix]
lib.determinant.restype = ctypes.c_int

lib.solution.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.solution.restype = ctypes.c_int


k = lib.solution(12 , -2, -20, -1)

P = np.array([[3, -1, -2], [2, 0, -1], [3, -5, 0]])
mat = matrix(*[ (ctypes.c_int * 3)(*row) for row in P ])

det_P = lib.determinant(mat)
det_Q = 2*k 
print("Determinant of P and Q = ", det_P)
print(det_Q*(det_P**2))
print(det_P*(det_Q**2))
