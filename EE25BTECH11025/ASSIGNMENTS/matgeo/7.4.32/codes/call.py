import ctypes as ct
import numpy as np

def get_results():
    lib = ct.CDLL("./problem.so")
    lib.get_results.argtypes = [ct.POINTER(ct.c_double)]

    data_type = ct.c_double * 19
    data = data_type()

    lib.get_results(data)

    arr = np.array(list(data))
    ratio, focus_x, focus_y, directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y= arr
    return ratio, np.array([focus_x, focus_y]), directrix_y, area, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, T1x, T1y, T2x, T2y, T3x, T3y
