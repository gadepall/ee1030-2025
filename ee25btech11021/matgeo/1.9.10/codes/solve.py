import ctypes

# Load shared library
lib = ctypes.CDLL("./libpoints.so")

# Define argument and return types
lib.distance.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.distance.restype = ctypes.c_double

lib.get_points.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.get_points.restype = None

# Prepare array for points
points = (ctypes.c_int * 4)()
lib.get_points(points)

x1, y1, x2, y2 = points
print(f"Point A = ({x1}, {y1})")
print(f"Point B = ({x2}, {y2})")

# Get distance
dist = lib.distance(x1, y1, x2, y2)
print(f"Distance between A and B = {dist}")

