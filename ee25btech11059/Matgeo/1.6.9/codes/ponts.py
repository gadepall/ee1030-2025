def check_collinearity_matrix(h, a, b, k):
    if h == 0 or k == 0:
        print("Invalid input: h and k must be non-zero.")
        return False

    # Step 1: Construct the matrix from vector differences
    row1_col1 = a - h
    row1_col2 = b
    row2_col1 = -h
    row2_col2 = k

    print("Collinearity matrix before row operations:")
    print(f"[ {row1_col1}\t{row1_col2} ]")
    print(f"[ {row2_col1}\t{row2_col2} ]")

    # Step 2: Simulate row operation R1 = R1 - R2
    new_r1_col1 = row1_col1 - row2_col1  # a
    new_r1_col2 = row1_col2 - row2_col2  # b - k

    print("\nAfter row operation R1 = R1 - R2:")
    print(f"[ {new_r1_col1}\t{new_r1_col2} ]")
    print(f"[ {row2_col1}\t{row2_col2} ]")

    # Step 3: Check the condition (a/h + b/k == 1) without floating point
    lhs = a * k + b * h
    rhs = h * k

    print("\nChecking condition: (a/h + b/k == 1)")
    print(f"Computed: ({a} * {k} + {b} * {h}) = {lhs}")
    print(f"Expected: ({h} * {k}) = {rhs}")

    return lhs == rhs

# Main function equivalent
if __name__ == "__main__":
    # Example input values (you can modify these)
    h = 5
    a = 2
    b = 3
    k = 4

    print("Checking collinearity for points:")
    print(f"A = ({h}, 0), B = ({a}, {b}), C = (0, {k})\n")

    if check_collinearity_matrix(h, a, b, k):
        print("\nPoints are collinear (Matrix rank = 1 and a/h + b/k = 1).")
    else:
        print("\nPoints are NOT collinear (Condition fails).")
