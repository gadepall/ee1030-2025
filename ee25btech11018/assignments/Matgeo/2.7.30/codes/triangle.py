import ctypes

# Load the shared library
lib = ctypes.CDLL("./triangle.so")

# Define return types
lib.solve_for_k.restype = ctypes.c_double
lib.calculate_area.restype = ctypes.c_double
lib.calculate_area.argtypes = [ctypes.c_double]

# Call the function to get k
k_value = lib.solve_for_k()
print(f"Calculated value of k: {k_value}")

# Verify by calculating the area
area = lib.calculate_area(k_value)
print(f"Area of the triangle with k={k_value}: {area}")

