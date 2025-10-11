import ctypes

# Load shared library
lib = ctypes.CDLL("./libplane.so")

# dot function
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.dot.restype = ctypes.c_double

# plane function (void, takes array of 3 doubles)
lib.plane.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.plane.restype = None

# Call plane (this will print from inside C)
arr = (ctypes.c_double * 3)(3.0, 1.0, 7.0)
lib.plane(arr)

