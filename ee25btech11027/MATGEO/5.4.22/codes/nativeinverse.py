def print_matrix(mat, title="Matrix:"):
    """
    A helper function to print a matrix in a readable format.
    """
    print(f"\n{title}")
    # Format to handle both integers and floats nicely
    for row in mat:
        print("  ".join(f"{num:8.3f}" for num in row))

def main():
    """
    Main function to get a 2x2 matrix from the user,
    calculate its inverse, and print the result.
    """
    matrix = []
    print("Enter the elements for the 2x2 matrix.")
    
    # Get user input with error handling
    for i in range(2):
        while True:
            try:
                # Allows entering a full row at once, e.g., "6.0 2.0"
                row_input = input(f"Enter the two elements of row {i+1} (separated by a space): ")
                row = [float(x) for x in row_input.split()]
                if len(row) != 2:
                    print("Error: Please enter exactly two numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    print_matrix(matrix, "Original Matrix:")

    # --- Calculation ---
    # Unpack the matrix elements:
    # | a  b |
    # | c  d |
    a, b = matrix[0]
    c, d = matrix[1]

    # 1. Calculate the determinant
    determinant = (a * d) - (b * c)
    print(f"\nDeterminant: {determinant:.3f}")

    # 2. Check if the matrix is invertible
    if determinant == 0:
        print("\nThis matrix is singular and has no inverse. ")
        return

    # 3. Calculate the inverse using the formula
    # Inverse = (1/determinant) * | d -b |
    #                             | -c a |
    inv_determinant = 1 / determinant
    
    inverse_matrix = [
        [d * inv_determinant, -b * inv_determinant],
        [-c * inv_determinant, a * inv_determinant]
    ]

    print_matrix(inverse_matrix, "Inverse Matrix:")

if __name__ == "__main__":
    main()
