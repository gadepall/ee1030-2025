import ctypes

# Load shared object
lib = ctypes.CDLL('./matrix_solver.so')

# Prepare result array
ResultArray = ctypes.c_double * 2
result = ResultArray()

# Call C function
lib.solve(result)

# Output
print("Solution:")
print(f"a = {round(result[0])}")
print(f"b = {round(result[1])}")
