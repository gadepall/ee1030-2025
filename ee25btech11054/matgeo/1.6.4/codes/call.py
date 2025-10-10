import ctypes

# Load shared library
lib = ctypes.CDLL("./libvectors.so")

# Set return types
lib.get_v1.restype = ctypes.POINTER(ctypes.c_double)
lib.get_v2.restype = ctypes.POINTER(ctypes.c_double)

# Extract vectors
v1 = [lib.get_v1()[i] for i in range(3)]
v2 = [lib.get_v2()[i] for i in range(3)]

print("Vector v1 =", v1)
print("Vector v2 =", v2)

