import ctypes

# Load the shared library
linecheck = ctypes.CDLL('./liblinecheck.so')

# Define argument and return types for the C function
linecheck.point_on_line.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
linecheck.point_on_line.restype = ctypes.c_int

# Example: line 3x+2y=4, check if (0,2) is on the line
n1 = 3
n2 = 2
x = 0
y = 2
c = 4

result = linecheck.point_on_line(n1, n2, x, y, c)
print("Point lies on line:" if result else "Point does not lie on line.")
