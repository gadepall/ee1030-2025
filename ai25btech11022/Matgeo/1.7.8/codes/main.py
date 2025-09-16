import ctypes

# Load the shared library
lib = ctypes.CDLL("./libmain.so")   

# Define argument and return types
lib.check_collinear.argtypes = (ctypes.c_int * 3 * 3,)  # 3x3 int array
lib.check_collinear.restype = ctypes.c_int

# Example points: three collinear points
pts = ((1, 2, 3),
       (2, 4, 6),
       (3, 6, 9))

# Convert Python tuple -> C array
c_pts = (ctypes.c_int * 3 * 3)(* [ (ctypes.c_int * 3)(*row) for row in pts ])

# Call C function
result = lib.check_collinear(c_pts)

if result == 1:
    print("Points are collinear")
else:
    print("Points are not collinear")
