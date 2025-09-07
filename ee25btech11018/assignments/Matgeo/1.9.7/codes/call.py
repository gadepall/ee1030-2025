import ctypes

# Load the shared library
lib = ctypes.CDLL("./libcodenorm.so")

# Set argument and return types for the function
lib.norm.argtypes = [ctypes.c_int, ctypes.c_int]
lib.norm.restype = ctypes.c_double

# Call the function
x, y = -6, 8
distance = lib.norm(x, y)
print(f"Therefore, the distance of the point ({x}, {y}) from the origin is {distance:.2f} units.")

