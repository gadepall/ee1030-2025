import ctypes

# Load the shared object file
lib = ctypes.CDLL('./distance.so')

# Set argument and return types
lib.point_to_line_distance.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                       ctypes.c_double, ctypes.c_double]
lib.point_to_line_distance.restype = ctypes.c_double

# Line: 3x - 4y - 26 = 0 → a=3, b=-4, c=-26
a, b, c = 3, -4, -26
px, py = 3, -5   # Point

# Call the C function
distance = lib.point_to_line_distance(a, b, c, px, py)
print(f"Distance from P({px},{py}) to line 3x-4y-26=0 is {distance}")
