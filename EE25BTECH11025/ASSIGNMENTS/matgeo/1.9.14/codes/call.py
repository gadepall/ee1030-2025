import ctypes as ct
import numpy as np

def get_data():
    lib = ct.CDLL("./problem.so")

    value = ct.c_double*9

    lib.make_data.argtypes = [ct.POINTER(ct.c_double)]

    points = value()

    lib.make_data(points)

    Px = points[0] 
    Py = points[1]
    Qx = points[2]
    Qy = points[3]
    Rx = points[4]
    Ry = points[5]
    Mx = points[6]
    My = points[7]
    values = points[8]
    return Px, Py, Qx, Qy, Rx, Ry, Mx, My, values








