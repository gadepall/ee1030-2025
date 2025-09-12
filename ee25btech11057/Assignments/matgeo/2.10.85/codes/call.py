import ctypes
import os

# Load shared library
lib = ctypes.CDLL(os.path.abspath("./libvolume.so"))

# Set return types
lib.get_determinant.restype = ctypes.c_double
lib.get_volume.restype = ctypes.c_double
lib.compute_volume.restype = ctypes.c_double
lib.get_u.restype = ctypes.c_double
lib.get_v.restype = ctypes.c_double
lib.get_w.restype = ctypes.c_double

# Fetch vectors u, v, w
u = [lib.get_u(i) for i in range(3)]
v = [lib.get_v(i) for i in range(3)]
w = [lib.get_w(i) for i in range(3)]

# Fetch determinant, volume, and final result
det = lib.get_determinant()
V = lib.get_volume()
result = lib.compute_volume()

# Print everything
print("Vector u =", u)
print("Vector v =", v)
print("Vector w =", w)
print("Determinant =", det)
print("Volume V =", V)
print("Final (80/3)*V =", result)

