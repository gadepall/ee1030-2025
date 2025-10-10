import ctypes
from ctypes import Structure, c_int

# Define the Point structure to match the C structure
class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

# Load the shared library
lib = ctypes.CDLL('./libfunc.so')

# Set the argument and return types for the function
lib.find_point_c.argtypes = [Point, Point, Point]
lib.find_point_c.restype = Point

# Define the points A, B, D
A = Point(3, 1)
B = Point(5, 1)
D = Point(4, 3)

# Call the function
C = lib.find_point_c(A, B, D)

# Print the result
print(f"Point C = ({C.x}, {C.y})")
