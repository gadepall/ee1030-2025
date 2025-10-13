import ctypes

# Load shared object
lib = ctypes.CDLL("./area_equal_division.so")

# Alternatively, define a function in C to return 'a' value only.

# Let's assume we modify the C file to have find_a() returning value.
lib.find_a = lib.find_a if hasattr(lib, 'find_a') else None

if lib.find_a:
    lib.find_a.restype = ctypes.c_double
    print("The value of a =", lib.find_a())
else:
    print("Run 'area_equal_division' directly as a C executable.")

