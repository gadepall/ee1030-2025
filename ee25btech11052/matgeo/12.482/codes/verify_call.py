import ctypes
import numpy as np # Used for sqrt for comparison

# 1. Load the shared library
lib = ctypes.CDLL('./eigen_solver_full.so')

# 2. Define the argument types for the C function
lib.find_eigen_system_2x2.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# 3. Create C-type variables to hold all results
eig_val1, eig_val2 = ctypes.c_double(), ctypes.c_double()
eig_vec1_x, eig_vec1_y = ctypes.c_double(), ctypes.c_double()
eig_vec2_x, eig_vec2_y = ctypes.c_double(), ctypes.c_double()

# 4. Call the C function for the matrix M = [[5, 3], [3, 5]]
lib.find_eigen_system_2x2(
    5.0, 3.0, 3.0, 5.0,
    ctypes.byref(eig_val1), ctypes.byref(eig_val2),
    ctypes.byref(eig_vec1_x), ctypes.byref(eig_vec1_y),
    ctypes.byref(eig_vec2_x), ctypes.byref(eig_vec2_y)
)

# 5. Determine which result corresponds to the smallest eigenvalue
if eig_val1.value < eig_val2.value:
    smallest_eigenvalue = eig_val1.value
    smallest_eigenvector = [eig_vec1_x.value, eig_vec1_y.value]
else:
    smallest_eigenvalue = eig_val2.value
    smallest_eigenvector = [eig_vec2_x.value, eig_vec2_y.value]

# 6. Print the results to verify
print(f"Smallest eigenvalue: {smallest_eigenvalue:.0f}")
print(f"Corresponding normalized eigenvector: [{smallest_eigenvector[0]:.7f}, {smallest_eigenvector[1]:.7f}]")

# Compare with the document's expected vector
print(f"\nDocument's vector: [ 1/sqrt(2), -1/sqrt(2) ]")
print(f"Numerical value:   [ {1/np.sqrt(2):.7f}, {-1/np.sqrt(2):.7f} ]")