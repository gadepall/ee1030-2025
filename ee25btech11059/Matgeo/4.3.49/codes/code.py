import numpy as np

def gauss_elimination(mat):
    mat = mat.astype(float)
    rows, cols = mat.shape

    # Forward elimination
    for i in range(min(rows, cols-1)):
        # Make pivot = 1
        if mat[i, i] != 0:
            mat[i] = mat[i] / mat[i, i]
        # Eliminate below
        for j in range(i+1, rows):
            mat[j] = mat[j] - mat[j, i] * mat[i]

    # Backward elimination
    for i in range(min(rows, cols-1)-1, -1, -1):
        for j in range(i-1, -1, -1):
            mat[j] = mat[j] - mat[j, i] * mat[i]

    return mat

def print_matrix(mat):
    for row in mat:
        print(" ".join(f"{val:6.2f}" for val in row))
    print()
