import numpy as np
from scipy.linalg import lu, solve_triangular

# Define the matrix A and vector b from the problem
A = np.array([
    [1, 1, 1],
    [2, 1, 2],
    [1, 3, 2]
], dtype=float)

b = np.array([1, 1, 1], dtype=float)

# Perform LU decomposition using SciPy.
# This returns P, L, U such that P @ A = L @ U.
# P keeps track of row swaps (pivoting).
P, L, U = lu(A)

print("## LU Decomposition with Pivoting (SciPy) ##\n")
# This P matrix tells you which rows were swapped.
print("Permutation Matrix (P):\n", P) 
# This L and U are for the ROW-SWAPPED version of A.
print("\nLower Triangular Matrix (L):\n", L)
print("\nUpper Triangular Matrix (U):\n", U)
print("-" * 35)

# Verify that P @ A = L @ U
print("Verification: P @ A equals L @ U is:", np.allclose(P @ A, L @ U))
print("-" * 35)


# --- Part a): Solve Lz = Pb ---
# To solve correctly, you MUST apply the same row swaps to b.
# Your code does this perfectly with P @ b.
Pb = P @ b
z = solve_triangular(L, Pb, lower=True)

print("\n## Part a): Solving Lz = Pb ##\n")
print("The solution vector z is:")
print(z) # Note: This z will be different from your manual one, because L is different.
print("-" * 35)


# --- Part b): Solve Ux = z ---
# The final step is the same.
x = solve_triangular(U, z, lower=False)

print("\n## Part b): Solving Ux = z ##\n")
print("The final solution vector x is:")
print(x) # This final answer WILL match your manual calculation!
print("-" * 35)
