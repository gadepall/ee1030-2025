import ctypes

lib = ctypes.CDLL('./code.so')
lib.direction_vec_x.argtypes = [ctypes.c_double, ctypes.c_double]
lib.direction_vec_x.restype = ctypes.c_double

lib.direction_vec_y.argtypes = [ctypes.c_double, ctypes.c_double]
lib.direction_vec_y.restype = ctypes.c_double

n = [-2, 3]
d = [lib.direction_vec_x(n[0], n[1]), lib.direction_vec_y(n[0], n[1])]

print("Normal vector: \n", n)
print("Direction vector: \n", d)