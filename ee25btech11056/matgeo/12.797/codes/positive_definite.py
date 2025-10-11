import ctypes
import numpy as np


# Load the compiled shared object file
lib = ctypes.CDLL("./positive_definite.so")

# Define the C function signature
# int check_statements(double A[][10], int n)
lib.check_statements.argtypes = [((ctypes.c_double * 10) * 10), ctypes.c_int]
lib.check_statements.restype = ctypes.c_int

# Define input matrix A (symmetric and positive definite)
# Example: A = [[2, 1], [1, 2]]
A_np = np.array([[2.0, 1.0],
                 [1.0, 2.0]], dtype=np.float64)
n = A_np.shape[0]

# Convert numpy matrix to C 2D array
A_c = ((ctypes.c_double * 10) * 10)()
for i in range(n):
    for j in range(n):
        A_c[i][j] = A_np[i][j]

# Call the C function
result = lib.check_statements(A_c, n)

# Display result
if result == 1:
    print("Both statements (I) and (II) are TRUE for the given matrix A.")
else:
    print("One or both statements are FALSE for the given matrix A.")

# Print the matrix for reference
print("Matrix A:")
print(A_np)


