import ctypes
import numpy as np
import math

r=math.sqrt(3)

#Load shared library
lib=ctypes.CDLL("./libangle.so")

#define function parameters
lib.angle.argtypes=[np.ctypeslib.ndpointer(dtype=np.double, ndim=1, shape=(2,)) ,
                    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, shape=(2,))]

lib.angle.restype=ctypes.c_double

#define input
n1=np.array([(2-r),-1],dtype=np.double)
n2=np.array([(2+r),-1],dtype=np.double)

# ensure contiguous memory
n1 = np.ascontiguousarray(n1, dtype=np.double)
n2 = np.ascontiguousarray(n2, dtype=np.double)

C=lib.angle(n1,n2)

print("angle is ",C)
