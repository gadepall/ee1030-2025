import ctypes
import numpy as np

# Load the shared library
lib_matrix = ctypes.CDLL("./code11.so")

# Define the argument types and return type for the C function
# findInverse takes the original matrix (input) and an empty matrix for the inverse (output)
lib_matrix.findInverse.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(3, 3), flags='C_CONTIGUOUS'), # input matrix
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(3, 3), flags='C_CONTIGUOUS')  # output inverse matrix
]
lib_matrix.findInverse.restype = ctypes.c_int # Returns 0 for success, 1 for error

# The matrix from the image:
# (1  1  -2)
# (2  1  -3)
# (5  4  -9)
original_matrix = np.array([
    [1.0, 1.0, -2.0],
    [2.0, 1.0, -3.0],
    [5.0, 4.0, -9.0]
], dtype=np.float64)

# Create an empty numpy array to store the result of the inverse
inverse_matrix_result = np.zeros((3, 3), dtype=np.float64)

print("Original Matrix:")
print(original_matrix)

# Call the C function to find the inverse
# The C function will populate inverse_matrix_result
success_code = lib_matrix.findInverse(original_matrix, inverse_matrix_result)

if success_code == 0:
    print("\nThe inverse of the matrix is:")
    print(inverse_matrix_result)

    # You can optionally verify the inverse by multiplying with the original matrix
    # (A * A_inv should be close to identity matrix)
    print("\nVerification (Original * Inverse):")
    print(np.dot(original_matrix, inverse_matrix_result))
else:
    print("\nCould not find the inverse as the matrix is singular (determinant is zero).")
