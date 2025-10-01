import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./code.so")

# Define argument and return types
lib.solve_system.argtypes = [np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")]
lib.solve_system.restype = None

# Prepare array to hold solution [x, y]
sol = np.zeros(2, dtype=np.double)

# Call the C function
lib.solve_system(sol)

# Print result
print("Solution of system:")
print("x =", sol[0])
print("y =", sol[1])
