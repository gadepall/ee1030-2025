import ctypes as ct
import numpy as np
import matplotlib.pyplot as plt

handc2 = ct.CDLL("./func.so")

handc2.calc.argtypes = [
    ct.POINTER(ct.c_double),
    ct.c_int,ct.c_int
]

handc2.calc.restype = ct.c_double

A = np.array([1,1,-1],dtype=np.float64).reshape(-1,1)
m = 3 ; 

ans = handc2.calc(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    m, 1
)

print("y[-1] = ",ans)

