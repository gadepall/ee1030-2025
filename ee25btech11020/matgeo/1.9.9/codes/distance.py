import ctypes
import numpy as np

d=ctypes.CDLL("./distance.so")

d.distance.argtypes=(ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double),ctypes.c_int)
d.distance.restype=ctypes.c_double

A = np.array([-7.0/3.0,5.0],dtype=np.double)
B = np.array([2.0/3.0,5.0],dtype=np.double)

result=d.distance(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),2)
print("Distance:",result)
