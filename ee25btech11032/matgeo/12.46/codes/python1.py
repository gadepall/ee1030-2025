import ctypes as ct
import numpy as np

handc1 = ct.CDLL("./func.so")

handc1.solve.argtypes = [
    ct.c_double,
    ct.c_double,
    ct.c_double,
    ct.POINTER(ct.c_double) 
]

A = np.zeros(2, dtype =np.float64).reshape(-1,1)

handc1.solve.restype = None
a , b, c = 1 , 1, -10
handc1.solve(
    a,b,c,
    A.ctypes.data_as(ct.POINTER(ct.c_double))
)

print("The Eigen values are : ",A)


