import ctypes
import numpy as np
from sympy import Matrix

def solve_and_prepare_data():

    lib = ctypes.CDLL('./code.so')
    double_array_8 = ctypes.c_double * 8
    lib.get_system_coeffs.argtypes = [ctypes.POINTER(ctypes.c_double)]
    out_data_c = double_array_8()
    lib.get_system_coeffs(out_data_c)
    raw_data = list(out_data_c)

    # Unpack the raw data
    m_coeffs = raw_data[0:4]
    c_coeffs = raw_data[4:6]
    a, b = raw_data[6], raw_data[7]

    aug_M = Matrix([
        [m_coeffs[0], m_coeffs[1], c_coeffs[0]],
        [m_coeffs[2], m_coeffs[3], c_coeffs[1]]
    ])

    rref_matrix, _ = aug_M.rref()
    solution_P = np.array(rref_matrix[:, -1]).flatten()

    x_start, x_end = -2.0, a + 2.0
    y1_start, y1_end = (b/a) * x_start, (b/a) * x_end
    y2_start, y2_end = (-a/b) * x_start + (a**2 + b**2)/b, (-a/b) * x_end + (a**2 + b**2)/b

    return {
        "line1_x": [x_start, x_end], "line1_y": [y1_start, y1_end],
        "line2_x": [x_start, x_end], "line2_y": [y2_start, y2_end],
        "solution_point": solution_P,
        "a": a, "b": b
    }
