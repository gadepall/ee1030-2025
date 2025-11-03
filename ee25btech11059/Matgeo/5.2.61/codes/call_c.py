import ctypes

# Load the shared object
lib = ctypes.CDLL("./code.so")

# Define return type and argument type of the exposed function
lib.solve_system.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_system.restype = None

# Prepare solution array
solution = (ctypes.c_double * 3)()

# Call C function
lib.solve_system(solution)

# Print the result
print("Solution of system:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")



