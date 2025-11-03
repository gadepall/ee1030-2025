import ctypes

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Call the function
lib.solve_vectors()
