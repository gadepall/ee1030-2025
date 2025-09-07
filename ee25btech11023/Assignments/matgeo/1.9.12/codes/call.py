import ctypes

def get_point_from_c():
    lib = ctypes.CDLL('./mid.so')
    
    # Define C variable types for the output
    xc_c = ctypes.c_double()
    yc_c = ctypes.c_double()
    
    # Call the C function
    lib.calculate_section_point(ctypes.byref(xc_c), ctypes.byref(yc_c))
    
    # Return the values
    return xc_c.value, yc_c.value
