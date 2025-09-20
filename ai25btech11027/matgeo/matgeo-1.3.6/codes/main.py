from ctypes import CDLL, c_int

# load shared library
lib = CDLL("./libgeometry.so")

# set signatures
lib.is_parallelogram.argtypes = [c_int * 8]
lib.is_parallelogram.restype = c_int
lib.is_rectangle.argtypes = [c_int * 8]
lib.is_rectangle.restype = c_int
lib.is_square.argtypes = [c_int * 8]
lib.is_square.restype = c_int

# directly give 8 integers: (x0,y0,x1,y1,x2,y2,x3,y3)
points = (c_int * 8)(6,2, 2,1, 1,5, 5,6)

print("Parallelogram?", bool(lib.is_parallelogram(points)))
print("Rectangle?", bool(lib.is_rectangle(points)))
print("Square?", bool(lib.is_square(points)))
