import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
double_array_4 = ctypes.c_double * 4
lib.get_system_coeffs.argtypes = [ctypes.POINTER(ctypes.c_double)]
out_data_c = double_array_4()

lib.get_system_coeffs(out_data_c)
coeffs = list(out_data_c)
M = np.linalg.inv([
    [coeffs[0], coeffs[1]],
    [coeffs[2], coeffs[3]],
])

print(M)
