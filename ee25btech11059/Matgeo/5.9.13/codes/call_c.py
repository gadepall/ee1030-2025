import ctypes

# Load the shared object file
lib = ctypes.CDLL('./libcode.so')

# Call the solve function
lib.solve()
