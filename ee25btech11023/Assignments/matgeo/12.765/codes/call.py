import ctypes
import numpy as np

def solve_least_squares():

    lib = ctypes.CDLL('./code.so')

    out_data = (ctypes.c_double * 6)()
    lib.get_vectors.argtypes = [ctypes.POINTER(ctypes.c_double)]
    lib.get_vectors(out_data)

    data = np.array(list(out_data))
    v1 = data[0:3]
    v2 = data[3:6]
    v2_dot_v2 = np.dot(v2, v2)
    v2_dot_v1 = np.dot(v2, v1)
    alpha = v2_dot_v1 / v2_dot_v2
    error_vec = v1 - (alpha * v2)

    return v1, v2, error_vec, alpha
