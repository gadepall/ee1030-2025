import ctypes
from ctypes import c_double, c_int, POINTER
import math

# Load the shared object
lib = ctypes.CDLL("./libvectors.so")

# Define Vector struct
class Vector(ctypes.Structure):
    _fields_ = [("x", c_double), ("y", c_double), ("z", c_double)]

# Define function signature
lib.check_conditions.argtypes = [Vector, Vector, Vector, POINTER(c_int)]
lib.check_conditions.restype = None

# Example unit vectors (satisfying a+b+c=0)
a = Vector(1, 0, 0)
b = Vector(-0.5, math.sqrt(3)/2, 0)
c = Vector(-0.5, -math.sqrt(3)/2, 0)

# Results array
results = (c_int * 4)()
lib.check_conditions(a, b, c, results)

options = ['a', 'b', 'c', 'd']
for i, res in enumerate(results):
    print(f"Option {options[i]}: {'True' if res else 'False'}")

