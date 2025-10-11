import ctypes
import os


matrix_lib = ctypes.CDLL('./mat.so')
# --- 2. Define C Function Signatures ---

Matrix3x3 = (ctypes.c_double * 3) * 3

matrix_lib.calculate_trace.argtypes = [Matrix3x3]
matrix_lib.calculate_trace.restype = ctypes.c_double


matrix_lib.calculate_determinant.argtypes = [Matrix3x3]
matrix_lib.calculate_determinant.restype = ctypes.c_double



A_python = [
    [3.0, 1.0, 2.0],
    [2.0, -3.0, -1.0],
    [1.0, 2.0, 1.0]
]


A_c_type = Matrix3x3()
for i, row in enumerate(A_python):
    for j, val in enumerate(row):
        A_c_type[i][j] = val


sum_of_eigenvalues = matrix_lib.calculate_trace(A_c_type)
product_of_eigenvalues = matrix_lib.calculate_determinant(A_c_type)




print("--- Calling C functions from 'mat.so' via Python ---")
print(f"Sum of Eigenvalues (Trace)       = {sum_of_eigenvalues:.2f}")
print(f"Product of Eigenvalues (Determinant) = {product_of_eigenvalues:.2f}")
print("------------------------------------------------------")

if sum_of_eigenvalues != 0:
    ratio = product_of_eigenvalues / sum_of_eigenvalues
    print(f"The ratio (Product / Sum) is: {ratio:.2f}")
else:
    print("The ratio is undefined because the sum of eigenvalues is zero.")


