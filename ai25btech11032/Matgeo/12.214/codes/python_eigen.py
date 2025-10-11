import numpy as np
import matplotlib.pyplot as plt

# Define the matrix
A = np.array([[3, 4],
              [4, -3]], dtype=float)

# Compute eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

print("Matrix A:\n", A)
print("\nEigenvalues:", eigvals)
print("\nEigenvectors (normalized, from NumPy):\n", eigvecs)

# ---- Force integer eigenvectors ----
# For eig = +5, eigenvector ~ (2,1)
v1 = np.array([2, 1], dtype=float)
# For eig = -5, eigenvector ~ (1,-2)
v2 = np.array([1, -2], dtype=float)

print("\nAdjusted Eigenvectors:")
print("Eigenvalue 5  :", v1)
print("Eigenvalue -5 :", v2)

# ---- Plot ----
plt.figure(figsize=(5,5))
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1,
           color="red", label="eig=5")
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1,
           color="blue", label="eig=-5")

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True)
plt.legend()
plt.title("Eigenvectors of A = [[3,4],[4,-3]] (integer form)")

# Save and show
plt.savefig("eigenvectors_problem_adjusted.png", dpi=300)
plt.show()

