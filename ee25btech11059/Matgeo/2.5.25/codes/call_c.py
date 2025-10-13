import ctypes

# Load the shared object file
lib = ctypes.CDLL('./code.so')

# Call the solve_vectors function (no args, no return)
lib.solve_vectors()
