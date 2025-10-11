import numpy as np

# ---- Example Usage ----
m_values = np.linspace(0.1, 5, 50)
determinants = []
inverse_norms = []

for m in m_values:
    A = np.array([[1, m], [4, 2]], dtype=float)  # parametric 2x2 matrix
    det = np.linalg.det(A)

    try:
        Inv = np.linalg.inv(A)
        norm_inv = np.linalg.norm(Inv)
    except np.linalg.LinAlgError:
        Inv = None
        norm_inv = np.nan

    determinants.append(det)
    inverse_norms.append(norm_inv)

# Print results
for i, m in enumerate(m_values):
    print(f"m = {m:.2f}, det(A) = {determinants[i]:.4f}, ||A^-1|| = {inverse_norms[i]:.4f}")

