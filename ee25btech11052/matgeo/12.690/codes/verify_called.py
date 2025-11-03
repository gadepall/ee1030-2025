import numpy as np
import ctypes


eigen_lib = ctypes.CDLL('./libeigen.so')


calculate_eigenvalues_c = eigen_lib.calculate_eigenvalues
# The C function expects a pointer to the matrix (2D double array)
# and a pointer to the results (1D double array).
calculate_eigenvalues_c.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=2, flags='C'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C')
]
# The function returns void.
calculate_eigenvalues_c.restype = None


# --- Step 3: Prepare the data in Python ---
x = 10.0
# The matrix must be of type float64 to match 'double' in C.
A = np.array([[x, -3.0], [3.0, 4.0]], dtype=np.float64)

# Create an empty NumPy array that the C function will fill.
eigenvalues_from_c = np.zeros(2, dtype=np.float64)


# --- Step 4: Call the C function from Python ---
calculate_eigenvalues_c(A, eigenvalues_from_c)


print("Matrix A:")
print(A)

print("\nEigenvalues from C function:")
print(eigenvalues_from_c)

