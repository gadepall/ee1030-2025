import ctypes
import numpy as np

x=np.double(input("Enter the x coordinate: "))
y=np.double(input("Enter the y coordinate: "))

# Load shared library
lib = ctypes.CDLL("./libcollinear.so")

# Define function prototype
lib.collinear.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, shape=(2,))]
lib.collinear.restype = None

# Example: Pass a point A(x, y)
A = np.array([x,y], dtype=np.double)

lib.collinear(A)
