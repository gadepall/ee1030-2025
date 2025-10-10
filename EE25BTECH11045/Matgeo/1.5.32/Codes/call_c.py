import ctypes

# Load the shared library
ratio_lib = ctypes.CDLL("./ratio.so")   # use "ratio.dll" on Windows

# Declare function argument & return types
ratio_lib.find_ratio.argtypes = [ctypes.c_double, ctypes.c_double,
                                 ctypes.c_double, ctypes.c_double]
ratio_lib.find_ratio.restype = ctypes.c_double

# Points (1, -3) and (4, 5)
x1, y1 = 1, -3
x2, y2 = 4, 5

# Call C function
ratio = ratio_lib.find_ratio(x1, y1, x2, y2)

print(f"The ratio in which the X-axis divides the line segment is {ratio:.2f} : 1")