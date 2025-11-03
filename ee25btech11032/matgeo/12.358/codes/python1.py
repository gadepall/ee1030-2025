import ctypes as ct
import numpy as np

handc1 = ct.CDLL("./func.so")

handc1.inv.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)    
]

A = np.array([1 , 5 ], dtype =np.float64).reshape(-1,1)
B = np.array([2 , 7 ], dtype =np.float64).reshape(-1,1)

handc1.inv.restype = None

handc1.inv(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
)


