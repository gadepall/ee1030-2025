import ctypes
import math

# Define a 2x2 matrix type using ctypes (array of arrays)
Matrix2x2 = (ctypes.c_double * 2) * 2

def print_matrix(name, matrix):
    print(f"{name} = ")
    for i in range(2):
        print(f"  | {matrix[i][0]:6.2f}  {matrix[i][1]:6.2f} |")

def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def transpose(in_matrix, out_matrix):
    out_matrix[0][0] = in_matrix[0][0]
    out_matrix[0][1] = in_matrix[1][0]
    out_matrix[1][0] = in_matrix[0][1]
    out_matrix[1][1] = in_matrix[1][1]

def inverse(in_matrix, out_matrix):
    det = determinant(in_matrix)
    if abs(det) < 1e-9:
        return False
    inv_det = 1.0 / det
    out_matrix[0][0] =  in_matrix[1][1] * inv_det
    out_matrix[0][1] = -in_matrix[0][1] * inv_det
    out_matrix[1][0] = -in_matrix[1][0] * inv_det
    out_matrix[1][1] =  in_matrix[0][0] * inv_det
    return True

def are_matrices_equal(A, B):
    for i in range(2):
        for j in range(2):
            if abs(A[i][j] - B[i][j]) > 1e-9:
                return False
    return True

def main():
    # Define matrix Q
    Q = Matrix2x2()
    Q[0][0], Q[0][1] = 1.0, -2.0
    Q[1][0], Q[1][1] = 2.0,  1.0

    print("Given Matrix Q:")
    print_matrix("Q", Q)

    # a) Check if Q == Q^T
    print("a) Checking if Q == Q^T ...")
    Q_T = Matrix2x2()
    transpose(Q, Q_T)
    print_matrix("Transpose Q^T", Q_T)
    print(f"Result: Statement (a) is {'TRUE' if are_matrices_equal(Q, Q_T) else 'FALSE'}.\n")

    # b) Check if Q == Q^-1
    print("b) Checking if Q == Q^-1 ...")
    Q_inv = Matrix2x2()
    if inverse(Q, Q_inv):
        print_matrix("Inverse Q^-1", Q_inv)
        print(f"Result: Statement (b) is {'TRUE' if are_matrices_equal(Q, Q_inv) else 'FALSE'}.\n")
    else:
        print("Inverse does not exist.")
        print("Result: Statement (b) is FALSE.\n")

    # c) & d) Check full rank and column dependency using determinant
    print("c/d) Checking rank and column dependency...")
    det = determinant(Q)
    print(f"Determinant of Q = {det:.2f}")

    if abs(det) > 1e-9:
        print("Result: Statement (c) is TRUE (Determinant is non-zero, so Q is of full rank).")
        print("Result: Statement (d) is FALSE (Columns are linearly independent).\n")
    else:
        print("Result: Statement (c) is FALSE (Determinant is zero, so Q is not of full rank).")
        print("Result: Statement (d) is TRUE (Columns are linearly dependent).\n")
    print("Conclusion: The only TRUE statement is (c).")

if __name__ == "__main__":
    main()
