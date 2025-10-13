import ctypes
# Load the shared library
lib = ctypes.CDLL("./gauss_solver.so")
# Prepare C variables
c = ctypes.c_double()
a = ctypes.c_double()

# Call the function
lib.solve_system(ctypes.byref(c), ctypes.byref(a))

print(f"Number of children (c) = {c.value}")
print(f"Amount (a) = {a.value}")
