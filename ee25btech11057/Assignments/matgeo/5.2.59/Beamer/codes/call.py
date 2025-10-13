import ctypes

# Load the shared object file
solver = ctypes.CDLL('./solve.so')

# Tell Python about the function signature
solver.solve_system.argtypes = [ctypes.POINTER(ctypes.c_double)]
solver.solve_system.restype = None

# Create an array of 3 doubles to hold the solution
solution = (ctypes.c_double * 3)()

# Call the C function
solver.solve_system(solution)

# Print the results
print("Solution from C shared object:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")

