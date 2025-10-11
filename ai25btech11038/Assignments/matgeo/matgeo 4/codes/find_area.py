import ctypes

# Load the compiled shared library
lib = ctypes.CDLL('./crossproduct.so')

# Define argument and return types
lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double

# Example coordinates
x1, y1 = 0.0, 0.0
x2, y2 = 4.0, 0.0
x3, y3 = 0.0, 3.0

# Call the C function
area = lib.triangle_area(x1, y1, x2, y2, x3, y3)
print("Area of the triangle:", area)
