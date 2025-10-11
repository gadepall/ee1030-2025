import ctypes as ct
import numpy as np


lib = ct.CDLL("./problem.so")

entry = ct.c_double*4

lib.define_matrix.argtypes = [ct.POINTER(ct.c_double)]

data = entry()

lib.define_matrix(data)

A = np.array([[data[0],data[1]],
                  [data[2],data[3]]])
    
Ainv = np.linalg.inv(A)

print("Inverse of given matrix is\n", Ainv)





