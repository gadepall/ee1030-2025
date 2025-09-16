
import ctypes
import numpy as np

def get_all_points():
  
        # Load the compiled C shared library
    lib = ctypes.CDLL('./coord.so')
 

    # The C function expects a pointer to an array of 10 doubles
    double_array_10 = ctypes.c_double * 10
    lib.calculate_parallelogram_coords.argtypes = [ctypes.POINTER(ctypes.c_double)]

    # Create the C-style array to pass to the function
    out_coords_c = double_array_10()

    # Call the C function, passing the C array by reference
    lib.calculate_parallelogram_coords(out_coords_c)

    # Convert the C array result back into a NumPy array
    # Reshape it to 5x2 (5 points, each with x and y)
    all_points = np.array(out_coords_c).reshape(5, 2)
    
    return all_points