import ctypes


# Load the shared object
lib = ctypes.CDLL("./direction_cosines.so")


# Define argument and return types
lib.direction_cosines.argtypes = [
ctypes.c_double, ctypes.c_double, ctypes.c_double,
ctypes.c_double, ctypes.c_double, ctypes.c_double,
ctypes.POINTER(ctypes.c_double),
ctypes.POINTER(ctypes.c_double),
ctypes.POINTER(ctypes.c_double)
]


# Prepare variables
l = ctypes.c_double()
m = ctypes.c_double()
n = ctypes.c_double()


# Call the function
lib.direction_cosines(-2, 4, -5, 1, 2, 3, ctypes.byref(l), ctypes.byref(m), ctypes.byref(n))


print("Direction cosines (C via .so):", (l.value, m.value, n.value))
