import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

# Folder to save figures
figs_folder = os.path.join("..", "figs")

# Load shared object
lib = ctypes.CDLL("./points.so")

# Define function signature
lib.eigen_2x2.argtypes = [
    (ctypes.c_double * 2) * 2,           # A matrix
    ctypes.POINTER(ctypes.c_double),     # eigenvalues[2]
    ctypes.POINTER((ctypes.c_double * 2) * 3)  # eigenvectors[3][2]
]
lib.eigen_2x2.restype = None

# Define matrix A = [[4,0],[0,4]]
A = ((ctypes.c_double * 2) * 2)()
A[0][0], A[0][1] = 4.0, 0.0
A[1][0], A[1][1] = 0.0, 4.0

# Allocate arrays for eigenvalues and eigenvectors
eigenvalues = (ctypes.c_double * 2)()
eigenvectors = ((ctypes.c_double * 2) * 3)()

# Call C function
lib.eigen_2x2(A, eigenvalues, eigenvectors)

# Convert results to Python lists
eigs = [eigenvalues[i] for i in range(2)]
vecs = [[eigenvectors[i][0], eigenvectors[i][1]] for i in range(3)]

print("Eigenvalues from C:", eigs)
print("Candidate eigenvectors from C:", vecs)

# Plot the eigenvectors with arrowheads
fig, ax = plt.subplots(figsize=(6, 6))

colors = ["red", "blue", "green"]
labels = ["v1 (1,0)", "v2 (-2,1)", "v3 (4,-3)"]

for i, v in enumerate(vecs):
    ax.arrow(0, 0, v[0], v[1], head_width=0.2, head_length=0.3, fc=colors[i], ec=colors[i])
    ax.text(v[0]-0.1 , v[1]+0.4, labels[i], fontsize=10, color=colors[i])

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

