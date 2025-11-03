import ctypes

# Load the shared library
lib = ctypes.CDLL("./perpendicular.so")

# Define argument and return types
lib.foot_and_length.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double)]

# Inputs
px, py, pz = 1.0, 1.5, 2.0
a, b, c, d = 2.0, -2.0, 4.0, 5.0

# Outputs
x0 = ctypes.c_double()
y0 = ctypes.c_double()
z0 = ctypes.c_double()
dist = ctypes.c_double()

# Call the C function
lib.foot_and_length(px, py, pz, a, b, c, d,
                    ctypes.byref(x0), ctypes.byref(y0), ctypes.byref(z0), ctypes.byref(dist))

print(f"Foot of perpendicular = ({x0.value:.4f}, {y0.value:.4f}, {z0.value:.4f})")
print(f"Length of perpendicular = {dist.value:.4f}")