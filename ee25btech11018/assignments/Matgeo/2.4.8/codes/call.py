import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./unitvector.so')

# Define argument and return types
lib.get_unit_vectors.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.get_unit_vectors.restype = None

# Create an array of 6 doubles to store results from C
result_arr = (ctypes.c_double * 6)()

# Call the C function
lib.get_unit_vectors(result_arr)

# Convert the result to numpy array for easy handling
results = np.array(result_arr)

if results[0] == -999:
    print("Error: vectors are parallel or no unique perpendicular vector.")
else:
    print(f"Positive unit vector: ({results[0]:.3f}, {results[1]:.3f}, {results[2]:.3f})")
    print(f"Negative unit vector: ({results[3]:.3f}, {results[4]:.3f}, {results[5]:.3f})")

