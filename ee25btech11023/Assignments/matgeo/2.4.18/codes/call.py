import ctypes
import numpy as np

def get_vectors_from_c():
    lib = ctypes.CDLL('./direction_vector.so')
    
    # Define the argument types (two pointers to double arrays)
    double_ptr = ctypes.POINTER(ctypes.c_double)
    lib.calculate_vectors.argtypes = [double_ptr, double_ptr]

    # Prepare numpy arrays to receive the C results
    m1_result = np.zeros(3, dtype=np.float64)
    m2_result = np.zeros(3, dtype=np.float64)

    # Call the C function
    lib.calculate_vectors(m1_result.ctypes.data_as(double_ptr), 
                          m2_result.ctypes.data_as(double_ptr))

    # Return the final vectors
    return m1_result, m2_result
