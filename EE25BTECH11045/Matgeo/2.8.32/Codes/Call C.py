import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load shared library
if platform.system() == "Windows":
    dist_lib = ctypes.CDLL("./distance.dll")
else:
    dist_lib = ctypes.CDLL("./distance.so")

# Function signature
dist_lib.extra_distance.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
dist_lib.extra_distance.restype = ctypes.c_double

# Call the C function
extra = dist_lib.extra_distance(2, 4,   # house
                                5, 8,   # bank
                                13, 14, # school
                                13, 26) # office

print("Extra distance travelled:", extra, "km")
