import numpy as np

def get_submatrix(matrix, skip_row, skip_col):
    """
    Returns a submatrix by skipping a specified row and column.
    Useful for calculating minors.
    """
    submatrix = []
    for r_idx, row in enumerate(matrix):
        if r_idx == skip_row:
            continue
        new_row = []
        for c_idx, val in enumerate(row):
            if c_idx == skip_col:
                continue
            new_row.append(val)
        submatrix.append(new_row)
    return np.array(submatrix)

def determinant_2x2(matrix):
    """
    Calculates the determinant of a 2x2 matrix.
    """
    return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

def determinant_3x3(matrix):
    """
    Calculates the determinant of a 3x3 matrix.
    """
    det = (matrix[0, 0] * (matrix[1, 1] * matrix[2, 2] - matrix[1, 2] * matrix[2, 1]) -
           matrix[0, 1] * (matrix[1, 0] * matrix[2, 2] - matrix[1, 2] * matrix[2, 0]) +
           matrix[0, 2] * (matrix[1, 0] * matrix[2, 1] - matrix[1, 1] * matrix[2, 0]))
    return det

def cofactor_matrix_3x3(matrix):
    """
    Calculates the cofactor matrix for a 3x3 matrix.
    Each element C_ij is (-1)^(i+j) * M_ij, where M_ij is the determinant
    of the 2x2 submatrix obtained by removing row i and column j.
    """
    cofactor_mat = np.zeros((3, 3), dtype=float)
    for r in range(3):
        for c in range(3):
            sub = get_submatrix(matrix, r, c)
            minor = determinant_2x2(sub)
            cofactor_mat[r, c] = ((-1)**(r + c)) * minor
    return cofactor_mat

def inverse_matrix_3x3(matrix):
    """
    Finds the inverse of a 3x3 matrix using the formula:
    A_inv = (1/det(A)) * adj(A)
    where adj(A) is the adjoint matrix, which is the transpose of the cofactor matrix.
    """
    if matrix.shape != (3, 3):
        raise ValueError("Input matrix must be 3x3.")

    det = determinant_3x3(matrix)

    if abs(det) < 1e-9:  # Check for near-zero determinant (singular matrix)
        print("Error: Determinant is zero or very close to zero. Inverse does not exist.")
        return None

    cofactor_mat = cofactor_matrix_3x3(matrix)
    adjoint_mat = cofactor_mat.T  # Adjoint is the transpose of the cofactor matrix

    inverse = (1 / det) * adjoint_mat
    return inverse

# The matrix from the image:
# (1  1  -2)
# (2  1  -3)
# (5  4  -9)
original_matrix = np.array([
    [1.0, 1.0, -2.0],
    [2.0, 1.0, -3.0],
    [5.0, 4.0, -9.0]
], dtype=float)

print("Original Matrix:")
print(original_matrix)

inverse_result = inverse_matrix_3x3(original_matrix)

if inverse_result is not None:
    print("\nThe inverse of the matrix is:")
    print(inverse_result)

    # Verification: Multiply original matrix by its inverse
    print("\nVerification (Original * Inverse):")
    print(np.dot(original_matrix, inverse_result))
