import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libeigen_solver.so")

# Prepare result arrays
eigenvalues = (ctypes.c_double * 3)()
eigenvectors = (ctypes.c_double * 9)()

# Call function
lib.solve_eigen(eigenvalues, eigenvectors)

# Convert to numpy
eigvals = np.array(eigenvalues)
eigvecs = np.array(eigenvectors).reshape(3,3, order="F")  # column-major


print("Eigenvalues:", np.round(np.flip(eigvals),0))
print("Eigenvectors:\n", np.round(eigvecs,3))

