from ctypes import CDLL, c_double

# Load the shared library 
lib = CDLL("./area.so")

# Set argument and return types
lib.area_under_line.argtypes = (c_double, c_double)
lib.area_under_line.restype = c_double

# Example usage
a, b = 2.0, 3.0
area = lib.area_under_line(a, b)

print(f"Area under y = x + 1 from {a} to {b} is {area:.6f}")
