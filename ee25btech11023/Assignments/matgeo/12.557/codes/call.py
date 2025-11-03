import ctypes
import numpy as np

def get_trace_of_power_matrix():

    lib = ctypes.CDLL('./code.so')

    double_array_4 = ctypes.c_double * 4
    lib.get_matrix_A.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array_4()
    lib.get_matrix_A(out_data_c)

    A = np.array(list(out_data_c)).reshape((2, 2))

    eigenvalues = np.linalg.eigvals(A)
    lambda_1, lambda_2 = eigenvalues
    trace_A_1000 = lambda_1**1000 + lambda_2**1000

    return A, (lambda_1, lambda_2), trace_A_1000

if __name__ == '__main__':
    matrix_A, eigs, final_trace = get_trace_of_power_matrix()
    l1, l2 = eigs
    print(f"\ntrace(A^1000) = ({l1.real:.0f})^1000 + ({l2.real:.0f})^1000")
