import numpy as np
from sympy import Matrix

# Define the matrix
A = np.array([[5, 3],
              [1, 3]], dtype=float)

# --- Using NumPy ---
# Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Using NumPy:")
for i in range(len(eigenvalues)):
    vec = eigenvectors[:, i]
    # Normalize vector
    norm_vec = vec / np.linalg.norm(vec)
    print(f"Eigenvalue: {eigenvalues[i]:.0f}  --> Normalized eigenvector: {norm_vec}")

# --- Using SymPy (symbolic check) ---
M = Matrix([[5, 3],
            [1, 3]])

eigs = M.eigenvects()

print("\nUsing SymPy:")
for val, mult, vecs in eigs:
    for v in vecs:
        # Normalize with sympy
        v_normalized = v.normalized()
        print(f"Eigenvalue: {val}  --> Normalized eigenvector: {v_normalized}")

