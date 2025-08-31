import ctypes

# Load the shared library
lib = ctypes.CDLL("./libMatgeo1.so")

# Declare return types and argument types
lib.get_dividing_point.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
lib.get_dividing_point.restype = None

lib.print_values.restype = None

# Call print_values() from the shared object
lib.print_values()

# Prepare variables for Px, Py
Px = ctypes.c_float()
Py = ctypes.c_float()

# Call get_dividing_point()
lib.get_dividing_point(ctypes.byref(Px), ctypes.byref(Py))

print(f"The dividing point is ({Px.value:.2f}, {Py.value:.2f})")
