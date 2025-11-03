import ctypes as ct
import numpy as np

handc1 = ct.CDLL("./func.so")

handc1.solve.argtypes = [
    ct.c_double,
    ct.c_double,
    ct.c_double,
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double)
]


#(k-1)(k^2-root(3)k+1)

real = np.zeros(2, dtype =np.float64).reshape(-1,1)
img = np.zeros(2, dtype =np.float64).reshape(-1,1)

handc1.solve.restype = None
a ,b, c = 1 , -3**(1/2) , 1
handc1.solve(
    a,b,c,
    real.ctypes.data_as(ct.POINTER(ct.c_double)),
    img.ctypes.data_as(ct.POINTER(ct.c_double))
print("Val 1 : 1" )
for i in range(2) : 
    print(f"Val {i+2} : {real[i]} + j{img[i]}")


