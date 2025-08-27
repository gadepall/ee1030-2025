# c_interface.py
# A simple wrapper for the section_formula_lib.so shared library.

import ctypes

def get_point_from_c():
    # Load the shared C library.
    lib = ctypes.CDLL('./section.so')

    # Prepare C-style double variables to hold the results.
    xc_c = ctypes.c_double()
    yc_c = ctypes.c_double()

    # Define the C function's argument types.
    lib.calculate_section_point.argtypes = [ctypes.POINTER(ctypes.c_double),
                                            ctypes.POINTER(ctypes.c_double)]

    # Call the C function, passing the memory addresses of our variables.
    lib.calculate_section_point(ctypes.byref(xc_c), ctypes.byref(yc_c))

    # Return the values that the C function wrote into our variables.
    return xc_c.value, yc_c.value