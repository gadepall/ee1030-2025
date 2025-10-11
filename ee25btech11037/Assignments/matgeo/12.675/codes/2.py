A_python = [
    [3.0, 1.0, 2.0],
    [2.0, -3.0, -1.0],
    [1.0, 2.0, 1.0]
]


sum_of_eigenvalues = A_python[0][0] + A_python[1][1] + A_python[2][2]


product_of_eigenvalues = (A_python[0][0] * (A_python[1][1] * A_python[2][2] - A_python[1][2] * A_python[2][1]) -
                        A_python[0][1] * (A_python[1][0] * A_python[2][2] - A_python[1][2] * A_python[2][0]) +
                        A_python[0][2] * (A_python[1][0] * A_python[2][1] - A_python[1][1] * A_python[2][0]))


print("--- Calculating directly in Python ---")
print(f"Sum of Eigenvalues (Trace)       = {sum_of_eigenvalues:.2f}")
print(f"Product of Eigenvalues (Determinant) = {product_of_eigenvalues:.2f}")
print("------------------------------------------------------")


if sum_of_eigenvalues != 0:
    ratio = product_of_eigenvalues / sum_of_eigenvalues
    print(f"The ratio (Product / Sum) is: {ratio:.2f}")
else:
    print("The ratio is undefined because the sum of eigenvalues is zero.")


