import ctypes
import numpy as np

def solve_matrix_equation():

    lib = ctypes.CDLL('./code.so')
    double_array_8 = ctypes.c_double * 8
    lib.get_matrices_data.argtypes = [ctypes.POINTER(ctypes.c_double)]

    out_data_c = double_array_8()
    lib.get_matrices_data(out_data_c)
    raw_data = np.array(list(out_data_c))

    A = raw_data[0:4].reshape((2, 2))
    Y = raw_data[4:8].reshape((2, 2))

    X = np.linalg.solve(A, Y)

    return X
if __name__ == '__main__':
    solution_X = solve_matrix_equation()

    a = solution_X[0, 1]
    b = solution_X[1,0]

    print(f"\nThis corresponds to: a={a:.2f}, b={b:.2f}")
