import numpy as np

def solve_eigenvalue_problem(matrix):
    A = np.array(matrix)
    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Input matrix must be square.")
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

matrix = np.array([[1, 3, -4],
                            [1, -3, 5],
                            [3, 1, 0]])

    print("Solving the eigenvalue problem for the matrix:")
    print(matrix)