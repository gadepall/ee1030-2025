import ctypes

# Load shared library
lib = ctypes.CDLL('./libsolver.so')

# Prepare variables
a = ctypes.c_double()
b = ctypes.c_double()
status = ctypes.c_int()

# Call C function
lib.solve_system(ctypes.byref(a), ctypes.byref(b), ctypes.byref(status))

# Check result
if status.value == 1:
    print(f"Solution from C: a = {a.value}, b = {b.value}")
else:
    print("No unique solution exists.")
