import ctypes as ct
import numpy as np

handc1 = ct.CDLL("./func.so")

handc1.det.argtypes = [
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)    
]

A = np.array([2 , 0 ], dtype =np.float64).reshape(-1,1)
B = np.array([3 , 7 ], dtype =np.float64).reshape(-1,1)

handc1.det.restype = ct.c_double

ans = handc1.det(
    A.ctypes.data_as(ct.POINTER(ct.c_double)),
    B.ctypes.data_as(ct.POINTER(ct.c_double)),
)

print("Product of eigen values :",ans)


