import ctypes 
import numpy as np

lib=ctypes.CDLL("./libltm.so")

lib.check_ltm.argtypes=(ctypes.c_int , ctypes.c_int, np.ctypeslib.ndpointer(dtype=np.float64, ndim=2 , flags="C_CONTIGUOUS"))

lib.check_ltm.restype= None

#Example
A=np.matrix([[2,0,0],[3,1,0],[8,7,6]]).astype(np.float64)

lib.check_ltm(A.shape[0],A.shape[1],A)
