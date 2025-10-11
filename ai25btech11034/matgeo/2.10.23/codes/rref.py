import sympy as sp

def solve_system():
    # Input dimensions
    m = int(input("Enter number of rows of A (equations): "))
    n = int(input("Enter number of columns of A (unknowns): "))

    print("\nEnter matrix A (row by row, you can use fractions like 1/3):")
    A_list = []
    for i in range(m):
        row_input = input(f"Row {i+1}: ").split()
        if len(row_input) != n:
            raise ValueError("Row length must equal number of columns")
        row = [sp.Rational(x) for x in row_input]
        A_list.append(row)

    print("\nEnter vector b (one value per row, fractions allowed):")
    b_list = []
    for i in range(m):
        val = input(f"b[{i+1}]: ")
        b_list.append([sp.Rational(val)])

    # Convert to Sympy matrices
    A = sp.Matrix(A_list)
    b = sp.Matrix(b_list)

    # Solve system
    try:
        sol = A.gauss_jordan_solve(b)
        print("\nSolution:")
        sp.pprint(sol)
    except ValueError:
        print("\nNo solution exists.")

# Run the solver
solve_system()

