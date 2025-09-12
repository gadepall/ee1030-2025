 
import ctypes
import numpy as np
 
def load_vectors_from_c():
     
    # Load the shared C library. Assumes the file exists.
    lib = ctypes.CDLL('./plane.so')

    # Define the C function signature
    get_vectors_c = lib.get_vectors
    get_vectors_c.argtypes = [ctypes.POINTER(ctypes.c_double)]
    get_vectors_c.restype = None

    # Create array in Python and call the C function to fill it with data
    vector_data = np.zeros(12, dtype=np.float64)
    get_vectors_c(vector_data.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

    # Reshape the data and return the individual vectors
    vectors_from_c = vector_data.reshape(4, 3)
    a, b, c, v = vectors_from_c[0], vectors_from_c[1], vectors_from_c[2], vectors_from_c[3]
    return a, b, c, v