import ctypes
import os

# Path to the compiled shared object
lib_path = os.path.abspath("./libtriangle.so")

# Load the shared library
lib = ctypes.CDLL(lib_path)

# Specify return type of the triangleArea function
lib.triangleArea.restype = ctypes.c_double

# Call the C function
area = lib.triangleArea()

# Print the solution
print("The area of the triangle formed by the given lines is:", area)

