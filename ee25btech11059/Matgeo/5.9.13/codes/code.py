def print_matrix(mat):
    for row in mat:
        print("  ".join(f"{val:8.3f}" for val in row))
    print()


def gaussian_elimination(mat):
    n = len(mat)

    for i in range(n):
        # Make the diagonal element 1
        factor = mat[i][i]
        mat[i] = [val / factor for val in mat[i]]

        # Eliminate below and above
        for j in range(n):
            if j != i:
                row_factor = mat[j][i]
                mat[j] = [mat[j][k] - row_factor * mat[i][k] for k in range(n + 1)]

        print(f"After making row {i+1} pivot and eliminating others:")
        print_matrix(mat)

    # Extract solution
    return [row[-1] for row in mat]


def main():
    # Augmented matrix: [A | B]
    matrix = [
        [1, 1, 1, 21],
        [4, 3, 2, 60],
        [6, 2, 3, 70]
    ]

    print("Initial Augmented Matrix:")
    print_matrix(matrix)

    solution = gaussian_elimination(matrix)

    variables = ['x', 'y', 'z']
    print("Solution:")
    for var, val in zip(variables, solution):
        print(f"{var} = {val:.2f}")


if __name__ == "__main__":
    main()
