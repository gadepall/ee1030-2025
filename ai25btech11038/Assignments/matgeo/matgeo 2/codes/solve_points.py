from ctypes import CDLL, c_double, byref
import math

# Load the shared library
lib = CDLL("./libfindpoints.so")

# Prepare arguments and return types
lib.find_x_axis_points.argtypes = [c_double, c_double, c_double,
                                   c_double, c_double]
# Actually we will pass pointers for x1, x2
# Adjust to use byref for output

# Prepare output variables
x1 = c_double()
x2 = c_double()

# Call the C function
lib.find_x_axis_points(c_double(7.0), c_double(-4.0), c_double(2.0*math.sqrt(5.0)),
                       byref(x1), byref(x2))

print(f"Points on X-axis: ({x1.value}, 0) and ({x2.value}, 0)")