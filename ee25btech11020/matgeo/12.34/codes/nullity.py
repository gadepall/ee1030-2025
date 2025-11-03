import ctypes

lib = ctypes.CDLL("./nullity.so")

lib.find_nullity.argtypes = [ctypes.c_double]
lib.find_nullity.restype = ctypes.c_int

k = 10.0
nullity = lib.find_nullity(k)

print(f"Nullity for A = {k}I is {nullity}")

