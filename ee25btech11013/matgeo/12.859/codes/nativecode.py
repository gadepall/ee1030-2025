import numpy as np

# Example 1: λ1 = 1
P1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Example 2: λ2 = -1
P2 = np.array([
    [-1, 0, 0],
    [0, 1, 0],
    [0, 0, -1]
])

# Function to verify orthogonality and eigenvalues
def verify_matrix(P, name):
    print(f"--- {name} ---")
    print("Matrix P:\n", P)

    # Check orthogonality
    PT_P = np.dot(P.T, P)
    print("\nP^T * P =\n", PT_P)

    # Check if PT_P is identity
    print("\nIs P^T * P = I ?", np.allclose(PT_P, np.eye(P.shape[0])))

    # Eigenvalues of P
    eigenvalues, _ = np.linalg.eig(P)
    print("\nEigenvalues of P:", eigenvalues)
    print()

# Verify both
verify_matrix(P1, "Example 1 (λ1 = 1)")
verify_matrix(P2, "Example 2 (λ2 = -1)")

