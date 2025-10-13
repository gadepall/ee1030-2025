import numpy as np
from numpy.linalg import inv, det, LinAlgError

def solve_matrix_problem():
    """
    Analyzes the matrix Q and verifies the given statements.
    """
    # Define the 2x2 matrix Q as a NumPy array
    Q = np.array([[1, -2],
                  [2, 1]])

    print(f"Given Matrix Q:\n{Q}\n")
    # --- a) Check if Q is equal to its transpose ---
    print("a) Checking if Q is equal to its transpose...")
    # In NumPy, the .T attribute gets the transpose
    Q_T = Q.T
    print(f"Transpose Q^T:\n{Q_T}")
    # np.array_equal safely checks if two arrays are element-wise equal
    is_equal_to_transpose = np.array_equal(Q, Q_T)
    print(f"Result: Statement (a) is {is_equal_to_transpose}.\n")

    # --- b) Check if Q is equal to its inverse ---
    print("b) Checking if Q is equal to its inverse...")
    try:
        # np.linalg.inv calculates the inverse
        Q_inv = inv(Q)
        print(f"Inverse Q^-1:\n{np.round(Q_inv, 2)}") # Round for cleaner display
        is_equal_to_inverse = np.array_equal(Q, Q_inv)
        print(f"Result: Statement (b) is {is_equal_to_inverse}.\n")
    except LinAlgError:
        # This block runs if the matrix has no inverse (is singular)
        print("Inverse does not exist.")
        print("Result: Statement (b) is False.\n")

    # --- c) & d) Check rank and column dependency via the determinant ---
    print("c/d) Checking for full rank and column dependency...")
    # np.linalg.det calculates the determinant
    q_det = det(Q)
    print(f"Determinant of Q = {q_det:.2f}")

    # A square matrix has full rank if its determinant is non-zero.
    # Its columns are linearly dependent if the determinant is zero.
    if abs(q_det) > 1e-9:  # Use tolerance for floating point comparison
        print("Result: Statement (c) is True (Determinant is non-zero, so Q is of full rank).")
        print("Result: Statement (d) is False (Columns are linearly independent).\n")
    else:
        print("Result: Statement (c) is False (Determinant is zero, so Q is not of full rank).")
        print("Result: Statement (d) is True (Columns are linearly dependent).\n")
    print("Conclusion: The only TRUE statement is (c).")


if _name_ == "_main_":
    solve_matrix_problem()