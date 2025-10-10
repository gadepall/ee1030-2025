 
import ctypes
import numpy as np
 
def load_vectors_from_c():
     
    # Load the shared C library. Assumes the file exists.
    lib = ctypes.CDLL('./plane.so')

    double_array_12=ctypes.c_double*12
    out_vectors=double_array_12()
    lib.get_vectors.argtypes=[ctypes.POINTER(ctypes.c_double)]
    lib.get_vectors(out_vectors)
    # Reshape the data and return the individual vectors
    out_vector = np.array(out_vectors).reshape(4, 3)
    a, b, c, v = out_vector[0], out_vector[1], out_vector[2], out_vector[3]
    return a, b, c, v
