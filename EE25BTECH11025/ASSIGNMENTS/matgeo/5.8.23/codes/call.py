import ctypes as ct
import numpy as np

def get_data():
    lib = ct.CDLL("./problem.so")
    points = ct.c_double*6
    lib.get_data.argtypes = [ct.POINTER(ct.c_double)]

    data = points()

    lib.get_data(data)

    A = np.array([[data[0],data[1]],
                  [data[2],data[3]]])
    B = np.array([[data[4]],
                  [data[5]]])
    Ainv = np.linalg.inv(A)

    C = np.dot(Ainv, B)

    
    E = np.array([data[0], data[1]])
    F = np.array([data[2], data[3]])
    M = B.ravel()
    D = C.ravel()
    
    return D, M, E, F

