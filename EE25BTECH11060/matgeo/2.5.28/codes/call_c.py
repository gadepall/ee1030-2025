import ctypes

# Load the shared C library
lib = ctypes.CDLL("./libprojection.so")   # use "projection.dll" on Windows

# Define argument and return types
lib.projection.argtypes = [ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double)]
lib.projection.restype = None

# Define vectors a and b
a = (ctypes.c_double * 3)(2, 3, 2)
b = (ctypes.c_double * 3)(2, 2, 1)
proj = (ctypes.c_double * 3)()

# Call C function
lib.projection(a, b, proj)

# Print result
print(f"Projection of a on b = ({proj[0]:.2f})i + ({proj[1]:.2f})j + ({proj[2]:.2f})k")
