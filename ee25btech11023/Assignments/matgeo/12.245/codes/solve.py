import ctypes
import numpy as np

lib = ctypes.CDLL('./code.so')
double_array_20 = ctypes.c_double * 20
lib.get_matrices.argtypes = [ctypes.POINTER(ctypes.c_double)]

out_data_c = double_array_20()
lib.get_matrices(out_data_c)
data = np.array(list(out_data_c))
options = data.reshape(5, 2, 2)

given = options[0]

trace = np.trace(given)
det = np.linalg.det(given)

match_index = -1
for i in range(1,4):
    if np.isclose(np.trace(options[i]),trace) and np.isclose(np.linalg.det(options[i]),det):
        print("Option",i,"is the correct answer ")
        break

