import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libfraction_matrix.so")

# Prepare 2x3 matrix
MatrixType = ctypes.c_double * 3 * 2
matrix = MatrixType()

# Call C function to generate matrix
lib.generate_matrix(matrix)

# Convert to numpy array
aug_matrix = np.array([[matrix[i][j] for j in range(3)] for i in range(2)])

# Solve system
A = aug_matrix[:, :2]
B = aug_matrix[:, 2]
solution = np.linalg.solve(A, B)
x, y = solution

print(f"The fraction is {x}/{y}")

# Optionally save fraction to file for plotting
with open("fraction.txt", "w") as f:
    f.write(f"{x} {y}")

