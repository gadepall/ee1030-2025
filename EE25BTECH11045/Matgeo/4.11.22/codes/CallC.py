import ctypes

# Load the shared library
lib = ctypes.CDLL("./parallelogram.so")   # use "parallelogram.dll" on Windows

# Define struct mapping in Python
class Point(ctypes.Structure):
    fields = [("x", ctypes.c_float),
                ("y", ctypes.c_float),
                ("z", ctypes.c_float)]

# Bind function signatures
lib.find_intersection.restype = Point
lib.print_equations.restype = None

# Call C functions
lib.print_equations()

intersection = lib.find_intersection()
print(f"Intersection of diagonals: ({intersection.x}, {intersection.y}, {intersection.z})")