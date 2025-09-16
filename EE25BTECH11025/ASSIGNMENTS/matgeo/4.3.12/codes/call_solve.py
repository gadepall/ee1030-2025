import ctypes
import numpy as np
import math

lib = ctypes.CDLL("./problem.so")

lib.insert_vector.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_double))
lib.insert_vector.restype = None

lib.get_vector.argtypes = (ctypes.c_int,)
lib.get_vector.restype = ctypes.POINTER(ctypes.c_double)

vectors = [
    [1, -2],
    [0, 2],
    [2, 0],
    [4, 0],
    [math.sqrt(2), 4*math.sqrt(2)],
    [1, 1],
]

for i, vec in enumerate(vectors):
    arr = (ctypes.c_double * 2)(*vec)
    lib.insert_vector(i, arr)

def get_vector(i):
    ptr = lib.get_vector(i)
    return np.ctypeslib.as_array(ptr, shape=(2, ))

all_vectors = [get_vector(i) for i in range(0, 6)]

n = get_vector(0)

for i in range(1, 6):
    v = get_vector(i)
    v_T = v.T
    res = n@v_T
    if(res==4):
        print(f"option ({i}) lies on the given line.")
    else:
        print(f"option ({i}) does not lie on the given line.") 

