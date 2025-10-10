import ctypes

# Load shared library
lib = ctypes.CDLL('./libconic.so')

# Call the function
lib.conic_equation()
