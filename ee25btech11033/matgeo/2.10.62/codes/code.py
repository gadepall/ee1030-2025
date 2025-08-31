import ctypes
import os

# Define the matrix A from our corrected example
# A = [[1, 0, 0], [0, -1, 0], [0, 0, -2]]
matrix_A = [1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, -2.0]

solver_lib = ctypes.CDLL('./code.so')


# --- Define the function signature for type safety ---
# The function takes two arguments: a pointer to a double and another pointer to a double.
solver_lib.find_eigenvalues_3x3.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
# The function returns void (None in Python).
solver_lib.find_eigenvalues_3x3.restype = None

# --- Prepare the arguments for the C function ---
# 1. The input matrix as a C-compatible array of doubles
MatrixArray = ctypes.c_double * 9
c_matrix = MatrixArray(*matrix_A)

# 2. The output array to store the eigenvalues
ResultArray = ctypes.c_double * 3
c_eigenvalues = ResultArray()

# --- Call the C function ---
solver_lib.find_eigenvalues_3x3(c_matrix, c_eigenvalues)

# --- Process and print the results ---
# Convert the C array back to a Python list
py_eigenvalues = [val for val in c_eigenvalues]

print("C function successfully executed.")
print(f"The matrix A was: \n[ {matrix_A[0]:.1f} {matrix_A[1]:.1f} {matrix_A[2]:.1f} ]\n[ {matrix_A[3]:.1f} {matrix_A[4]:.1f} {matrix_A[5]:.1f} ]\n[ {matrix_A[6]:.1f} {matrix_A[7]:.1f} {matrix_A[8]:.1f} ]\n")
print(f"The calculated eigenvalues (λ) are: {py_eigenvalues}")