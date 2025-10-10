
import ctypes
import numpy as np

def get_line_data_from_c():

    lib = ctypes.CDLL('./coord.so')
    double_array_9 = ctypes.c_double * 9
    lib.get_intersection_data.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array_9()
    
    lib.get_intersection_data(out_data_c)
 
    all_data = np.array(out_data_c)
    
    # Split the data into the three vectors
    intersection_P = all_data[0:3]
    point_a = all_data[3:6]
    dir_d = all_data[6:9]
    
    return intersection_P, point_a, dir_d