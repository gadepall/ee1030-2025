import ctypes

# Load C shared library
lib = ctypes.CDLL("./points.so")

# Prepare ctypes doubles
n1 = ctypes.c_double()
n2 = ctypes.c_double()

# Call C function
lib.get_normal_vector(ctypes.byref(n1), ctypes.byref(n2))
print("Normal vector from C:", n1.value, n2.value)

# Save normal vector for plotting
normal_vector = (n1.value, n2.value)

