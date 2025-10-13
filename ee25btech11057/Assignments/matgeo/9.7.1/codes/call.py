import ctypes
import os

# Load the compiled shared object (.so file)
# Make sure "area_region.so" is in the same directory
so_file = "./area_region.so"

# Load the shared object
lib = ctypes.CDLL(so_file)

# Define the argument and return types for the C function 'main'
lib.main.restype = ctypes.c_int

print("Running the C integration program...\n")

# Call the main() function from the C program
lib.main()

