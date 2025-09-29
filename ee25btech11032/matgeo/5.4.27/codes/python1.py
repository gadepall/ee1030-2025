import ctypes as ct
import numpy as np

handc1 = ct.CDLL("./func.so")

handc1.inv.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)
]

A = np.array([2 , 5 , 0 ], dtype =np.float64).reshape(-1,1)
B = np.array([0 , 1 , 1 ], dtype =np.float64).reshape(-1,1)
C = np.array([-1 , 0 , 3 ], dtype =np.float64).reshape(-1,1)

handc1.inv.restype = None

handc1.inv(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
    C.ctypes.data_as(ct.POINTER(ct.c_double))
)


