import ctypes

# Define a 2x2 matrix structure that is compatible with the C struct
class Matrix2x2(ctypes.Structure):
    """A C-compatible 2x2 matrix structure."""
    fields = [
        ("elements", (ctypes.c_double * 2) * 2)
    ]

# --- Python functions that operate on the C-like structure ---

def print_matrix(m: Matrix2x2):
    """Prints the elements of a Matrix2x2 structure."""
    for i in range(2):
        for j in range(2):
            # Use an f-string for formatted output, similar to printf
            print(f"{m.elements[i][j]:8.2f}", end="")
        print()

def is_symmetric(m: Matrix2x2) -> bool:
    """
    Checks if a 2x2 matrix is symmetric.
    A matrix A is symmetric if element [0][1] equals element [1][0].
    """
    return m.elements[0][1] == m.elements[1][0]

def determinant(m: Matrix2x2) -> float:
    """
    Calculates the determinant of a 2x2 matrix.
    For a matrix [[a, b], [c, d]], the determinant is ad - bc.
    """
    return (m.elements[0][0] * m.elements[1][1]) - (m.elements[0][1] * m.elements[1][0])

# --- Main execution block, similar to C's main() function ---

if _name_ == "_main_":
    # Example 1: A real symmetric matrix that IS invertible
    # Instantiate the structure using nested tuples for the 2D array
    matrix_a = Matrix2x2(elements=((3.0, 1.0), (1.0, 2.0)))

    print("## Matrix A ##")
    print_matrix(matrix_a)
    # Use a ternary operator in the f-string to mimic C's output
    print(f"Is symmetric? {'Yes' if is_symmetric(matrix_a) else 'No'}")

    det_a = determinant(matrix_a)
    print(f"Determinant: {det_a:.2f}")
    print(f"Is invertible? {'Yes' if det_a != 0 else 'No'}\n")


    # Example 2: A real symmetric matrix that is NOT invertible
    matrix_b = Matrix2x2(elements=((2.0, 4.0), (4.0, 8.0)))

    print("## Matrix B ##")
    print_matrix(matrix_b)
    print(f"Is symmetric? {'Yes' if is_symmetric(matrix_b) else 'No'}")

    det_b = determinant(matrix_b)
    print(f"Determinant: {det_b:.2f}")
    print(f"Is invertible? {'Yes' if det_b != 0 else 'No'}")