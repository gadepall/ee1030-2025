import ctypes
import numpy as np

# Load the shared object
lib = ctypes.CDLL("./line_solver.so")

# Define function signatures
lib.gaussElimination.argtypes = [((ctypes.c_float * 3) * 2)]
lib.printMatrix.argtypes = [((ctypes.c_float * 3) * 2)]

def to_c_matrix(py_mat):
    """Convert Python 2x3 list into C float[2][3]"""
    c_mat = ((ctypes.c_float * 3) * 2)()
    for i in range(2):
        for j in range(3):
            c_mat[i][j] = py_mat[i][j]
    return c_mat

def to_py_matrix(c_mat):
    """Convert C float[2][3] back to Python list"""
    return [[c_mat[i][j] for j in range(3)] for i in range(2)]

# Case (a): slope=1/2, y-intercept=-3/2
mat1 = [[0, 1, -1.5],
        [1, -0.5, 0]]

c_mat1 = to_c_matrix(mat1)
print("Case (a): before elimination:")
lib.printMatrix(c_mat1)

lib.gaussElimination(c_mat1)

print("Case (a): after elimination:")
lib.printMatrix(c_mat1)
print("Python Matrix:", to_py_matrix(c_mat1))

# Case (b): slope=1/2, x-intercept=4
mat2 = [[4, 1, 0],
        [1, -0.5, 0]]

c_mat2 = to_c_matrix(mat2)
print("\nCase (b): before elimination:")
lib.printMatrix(c_mat2)

lib.gaussElimination(c_mat2)

print("Case (b): after elimination:")
lib.printMatrix(c_mat2)
print("Python Matrix:", to_py_matrix(c_mat2))
