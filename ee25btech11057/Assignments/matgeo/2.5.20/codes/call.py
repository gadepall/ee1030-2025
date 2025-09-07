import ctypes
import os
import math

# Load the shared library (ensure libvector.so is in the same directory)
lib_path = os.path.abspath("./libvector.so")
lib = ctypes.CDLL(lib_path)

# Tell Python the return type of the C function
lib.compute_magnitude.restype = ctypes.c_double

# Call the function from the shared object
result = lib.compute_magnitude()

# Print result
print("The magnitude of (3a - 2b + 2c) is:", result)

# (Optional) Verify using Python math
print("Verification using Python math.sqrt(61):", math.sqrt(61))

