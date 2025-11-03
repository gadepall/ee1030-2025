import ctypes
import numpy as np

def get_data_from_c():
    lib = ctypes.CDLL('./code.so')
    data_size = 2 + (101 * 2)
    double_array = ctypes.c_double * data_size
    lib.get_tangent_data.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array()
    lib.get_tangent_data(out_data_c)

    all_data = np.array(out_data_c)
    tangent_point = all_data[0:2]
    curve_points = all_data[2:].reshape((-1, 2))
    return tangent_point, curve_points
