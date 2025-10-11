import ctypes as ct
import numpy as np

def get_data():
    lib = ct.CDLL("./problem.so")

    points = ct.c_double*6

    lib.get_data.argtypes = [ct.POINTER(ct.c_double)]

    data = points()

    lib.get_data(data)

    fpoints = np.array(data)

    P = fpoints[0:2]
    A = fpoints[2:4]
    B = fpoints[4:6]
    return P, A, B

