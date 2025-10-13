import ctypes
import numpy as np

def calculate():
    lib = ctypes.CDLL('./code.so')
    double_array_12 = ctypes.c_double * 12
    lib.get_eigen_data.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array_12()
    lib.get_eigen_data(out_data_c)
    raw_data = np.array(list(out_data_c))

    eigenvalues = raw_data[0:3]
    v1 = raw_data[3:6]
    v2 = raw_data[6:9]
    v3 = raw_data[9:12]

    D = np.diag(eigenvalues)
    P = np.vstack([v1, v2, v3]).T
    P_inv = np.linalg.inv(P)
    A = P @ D @ P_inv
    result_6A = 6 * A

    return result_6A

if __name__ == '__main__':
    final_result = calculate()
    print("\n 6A =\n", final_result)
