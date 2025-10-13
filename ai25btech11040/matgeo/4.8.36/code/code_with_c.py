import ctypes

lib = ctypes.CDLL('./code.so')
lib.cross_x.argtypes = [ctypes.c_double]*6
lib.cross_x.restype = ctypes.c_double
lib.cross_y.argtypes = [ctypes.c_double]*6
lib.cross_y.restype = ctypes.c_double
lib.cross_z.argtypes = [ctypes.c_double]*6
lib.cross_z.restype = ctypes.c_double
lib.norm.argtypes = [ctypes.c_double]*3
lib.norm.restype = ctypes.c_double

A = [3, -1, 2]
B = [5, 2, 4]
C = [-1, -1, 6]
P = [6, 5, 9]

m = [a - b for a, b in zip(A, B)]
n = [a - b for a, b in zip(A, C)]

n = [lib.cross_x(m[0], m[1], m[2], n[0], n[1], n[2]),
     lib.cross_y(m[0], m[1], m[2], n[0], n[1], n[2]),
     lib.cross_z(m[0], m[1], m[2], n[0], n[1], n[2])]
print(f"Normal vector: {n}")

# Substitute point to find constant
c = sum([a*b for a, b in zip(n, A)])
print(f"Constant: {c}")

d = abs(sum([a*b for a,b in zip(n, P)]) - c)/lib.norm(n[0], n[1], n[2])

print("Distance of point P from plane:", d)