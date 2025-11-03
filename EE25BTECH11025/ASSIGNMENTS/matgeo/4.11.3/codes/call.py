import ctypes as ct
import numpy as np
import os

def get_data():
    libpath = os.path.join(os.path.dirname(__file__), "problem.so")
    lib = ct.CDLL(libpath)
    N = 18
    c_arr_type = ct.c_double * N
    lib.get_data.argtypes = [ct.POINTER(ct.c_double)]
    lib.get_data.restype = None
    c_arr = c_arr_type()
    lib.get_data(c_arr)
    data = np.array(c_arr, dtype=float)
    P0 = data[0:3]
    P1 = data[3:6]
    Q1 = data[6:9]
    Q2 = data[9:12]
    Q3 = data[12:15]
    X  = data[15:18]
    return P0, P1, Q1, Q2, Q3, X
