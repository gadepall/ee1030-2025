import numpy as np

# 1. Create a real symmetric matrix.
# Notice how it's symmetrical across the main diagonal.
A = np.array([
    [5, -2, 0],
    [-2, 9, 1],
    [0, 1, 4]
])

print("## Verifying Eigenvalues of a Real Symmetric Matrix ##\n")
print("Our Matrix A:\n", A)

# Verify that it is indeed symmetric
is_symmetric = np.allclose(A, A.T)
print("\nIs the matrix symmetric?", is_symmetric)
print("-" * 50)


# 2. Calculate the eigenvalues using NumPy.
# The result might be complex numbers (e.g., 5.1+0.j) for general matrices.
eigenvalues = np.linalg.eigvals(A)

print("\nCalculated Eigenvalues:\n", eigenvalues)
print("-" * 50)


# 3. Check if the eigenvalues are real.
# The proof guarantees that the imaginary part of each eigenvalue is zero.
all_eigenvalues_are_real = True
for lam in eigenvalues:
    # We use np.isclose instead of == 0 because of tiny floating-point errors.
    if not np.isclose(lam.imag, 0):
        all_eigenvalues_are_real = False
        break

print(f"\nConclusion: Are all eigenvalues real?")
print(f"--> {all_eigenvalues_are_real}")

if all_eigenvalues_are_real:
    print("\nAs the proof predicted, all the imaginary parts are zero!")
    print("The real eigenvalues are:", eigenvalues.real)
