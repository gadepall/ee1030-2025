import ctypes

# Load the shared library (change to .dll if using Windows)
lib = ctypes.CDLL("./plane_intercepts.so")

# Define function prototype
lib.find_intercepts.argtypes = [ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double)]

# Prepare variables
x = ctypes.c_double()
y = ctypes.c_double()
z = ctypes.c_double()

# Call C function
lib.find_intercepts(ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))

# Print results
print("X-intercept:", (x.value, 0, 0))
print("Y-intercept:", (0, y.value, 0))
print("Z-intercept:", (0, 0, z.value))