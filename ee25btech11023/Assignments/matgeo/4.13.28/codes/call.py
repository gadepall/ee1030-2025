import ctypes
import numpy as np

def get_data_from_c():
    
    lib = ctypes.CDLL('./code.so')
    
    double_array_8 = ctypes.c_double * 8
    lib.calculate_slope_data.argtypes = [ctypes.POINTER(ctypes.c_double)]
    
    out_data_c = double_array_8()
    lib.calculate_slope_data(out_data_c)
    
    all_data = np.array(out_data_c)
    
    # Unpack the data
    point_p = all_data[0:2]
    point_q1 = all_data[2:4]
    point_q2 = all_data[4:6]
    slopes = all_data[6:8]
    
    return point_p, point_q1, point_q2, slopes