def print_matrix(name: str, matrix: list[list[float]]):
    """Prints a 2x2 matrix with a given name in a formatted way."""
    print(f"Matrix {name}:")
    for row in matrix:
        print("  [ ", end="")
        for val in row:
            # Format to 2 decimal places with a width of 5 characters
            print(f"{val:5.2f} ", end="")
        print("]")
    print()

def analyze_lu_factorization(matrix_name: str, A: list[list[float]]):
    """
    Analyzes the LU factorization for a 2x2 matrix A.

    It checks the conditions derived from A = LU, where L is lower
    triangular with 1s on the diagonal and U is upper triangular.
    """
    print(f"--- Analyzing Matrix {matrix_name} ---")
    print_matrix(matrix_name, A)

    # For a matrix A = [[a, b], [c, d]], we want to find L and U such that A = LU:
    # L = [[1, 0], [l21, 1]] and U = [[u11, u12], [0, u22]]
    #
    # Multiplying L and U and equating to A gives the system of equations:
    # 1) u11 = A[0][0]
    # 2) u12 = A[0][1]
    # 3) l21 * u11 = A[1][0]  <-- This is the critical equation.
    # 4) l21 * u12 + u22 = A[1][1]

    u11 = A[0][0]
    a10 = A[1][0] # The element at row 1, column 0

    print("From the definition, the critical equation is: l21 * u11 = A[1][0]")
    print(f"Substituting known values from matrix {matrix_name}:")
    print(f"  -> l21 * {u11:.2f} = {a10:.2f}\n")

    # Check the condition of the critical equation (3)
    if u11 == 0:
        if a10 == 0:
            # This is the case for Matrix P: l21 * 0 = 0
            print(f"Result for {matrix_name}:")
            print("The equation becomes 0 = 0, which is always true.")
            print("This means 'l21' can be any real number, leading to infinitely many solutions.")
            print(f"Conclusion: Statement {matrix_name} is TRUE.")
        else:
            # This is the case for Matrix Q: l21 * 0 = 2
            print(f"Result for {matrix_name}:")
            print(f"The equation becomes 0 = {a10:.2f}, which is a contradiction.")
            print("No value of 'l21' can satisfy this, so no LU factorization exists.")
            print(f"Conclusion: Statement {matrix_name} is TRUE.")
    else:
        # This is the standard case where a unique solution would exist
        print(f"Result for {matrix_name}:")
        print(f"Since u11 ({u11:.2f}) is non-zero, a unique solution for l21 could be found.")
        print(f"This case does not apply to matrices P or Q.")
# This block ensures the code runs only when the script is executed directly
if _name_ == "_main_":
    # Matrix from Statement P
    P = [
        [0.0, 5.0],
        [0.0, 7.0]
    ]

    # Matrix from Statement Q
    Q = [
        [0.0, 0.0],
        [2.0, 5.0]
    ]
    
    print("This program analyzes the LU factorization for the two given matrices.\n")

    # Analyze Matrix P
    analyze_lu_factorization("P", P)

    # Analyze Matrix Q
    analyze_lu_factorization("Q", Q)

    print("Final Conclusion:")
    print("Both statements P and Q are TRUE. The correct option is (b).")