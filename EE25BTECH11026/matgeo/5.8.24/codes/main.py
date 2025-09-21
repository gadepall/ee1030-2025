import ctypes

# Load shared library
lib = ctypes.CDLL("./libgauss_solver.so")

# Define function signature
lib.solve_problem.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.solve_problem.restype = None

# Prepare result array
result = (ctypes.c_double * 2)()

# Call C function
lib.solve_problem(result)

ani_age = result[0]
bijoya_age = result[1]

print(f"Ani's age = {ani_age:.0f}")
print(f"bijoya's age = {bijoya_age:.0f}")
