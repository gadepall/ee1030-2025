import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Define matrix A = [[4,0],[0,4]]
A = np.array([[4.0, 0.0],
              [0.0, 4.0]])

# Compute eigenvalues and eigenvectors
eigs, _ = np.linalg.eig(A)

# Candidate eigenvectors given in the options
vecs = [
    [1, 0],   # option a
    [-2, 1],  # option b
    [4, -3]   # option c
]

print("Eigenvalues:", eigs)
print("Candidate eigenvectors:", vecs)

# Plot the eigenvectors with arrowheads
fig, ax = plt.subplots(figsize=(6, 6))

colors = ["red", "blue", "green"]
labels = ["v1 (1,0)", "v2 (-2,1)", "v3 (4,-3)"]

for i, v in enumerate(vecs):
    ax.arrow(0, 0, v[0], v[1], head_width=0.2, head_length=0.3,
             fc=colors[i], ec=colors[i])
    ax.text(v[0]-0.1, v[1]+0.4, labels[i], fontsize=10, color=colors[i])

# Axes setup
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect("equal")
ax.set_title("Eigenvectors of Matrix A")
ax.grid(True)

# Save figure
plt.tight_layout()
fig.savefig(os.path.join(figs_folder, "eigenvectors.png"))
plt.show()

