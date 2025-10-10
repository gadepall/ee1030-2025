 
import ctypes
import numpy as np

def get_vectors_from_c():
   
    
    lib = ctypes.CDLL('./vector.so')
    
    # The C function expects a pointer to a C double array of size 6
    double_array_6 = ctypes.c_double * 6
    lib.get_line_vectors.argtypes = [ctypes.POINTER(ctypes.c_double)]
    
    # Create the C-style array to receive the output data
    out_data_c = double_array_6()
    
    # Call the C function, which will fill the array
    lib.get_line_vectors(out_data_c)
    
    # Convert the C array back into a NumPy array
    all_data = np.array(out_data_c)
    
    # Split the data into the point vector and direction vector
    point_a = all_data[:3]
    dir_b = all_data[3:]
    
    return point_a, dir_b