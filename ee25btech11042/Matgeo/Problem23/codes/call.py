import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./12.159.so")

# Define the argument and return types for our C function
lib.determinant_3x3.argtypes = [ctypes.c_double * 9]
lib.determinant_3x3.restype = ctypes.c_double

# The 'b' variable from your problem
b = 0.0 # You can change this value to test other cases

# Define the matrix from the problem
# A = [[1+b, b, 1], [b, 1+b, 1], [1, 2b, 1]]
matrix_data = [
    1 + b, b, 1,
    b, 1 + b, 1,
    1, 2 * b, 1
]

# Convert the Python list to a C-style array of doubles
matrix_c = (ctypes.c_double * 9)(*matrix_data)

# Call the C function
determinant_value = lib.determinant_3x3(matrix_c)

# Print the result
print(f"The matrix (for b={b}):")
matrix_np = np.array(matrix_data).reshape(3, 3)
print(matrix_np)
print(f"\nDeterminant calculated from C function: {determinant_value}")
