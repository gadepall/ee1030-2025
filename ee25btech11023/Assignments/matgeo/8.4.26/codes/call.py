import ctypes
import numpy as np

def get_data_from_c():
    lib = ctypes.CDLL('./code.so')

    data_size = 2 + (2 * 51 * 2)
    double_array = ctypes.c_double * data_size
    lib.get_plot_data.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array()
    lib.get_plot_data(out_data_c)

    return np.array(out_data_c)
