import ctypes
import numpy as np
import os

so_file = os.path.abspath('./code.so')
lib = ctypes.CDLL(so_file)

# define C double arrays
class DoubleArray2(ctypes.Structure):
    _fields_ = [("arr", ctypes.c_double * 2)]
def create_double2(np_array):
    array_type = ctypes.c_double * 2
    return array_type(*np_array)

# C function
double2 = ctypes.c_double * 2
points_type = double2 * 2

find_points = lib.find_points
find_points.argtypes = [double2, double2, points_type]
find_points.restype = None

def get_points(x_vals, y_vals):
    x_c = double2(*x_vals)
    y_c = double2(*y_vals)
    out = points_type()
    find_points(x_c, y_c, out)
    result = np.array([[out[i][0], out[i][1]] for i in range(2)])
    return result

if __name__ == '__main__':
    x_vals = [1.0, 4.0]
    y_vals = [1.0, 4.0]
    pts = get_points(x_vals, y_vals)
    print(pts)

