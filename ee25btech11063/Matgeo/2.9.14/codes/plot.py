import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Given adjacent sides
a = np.array([2, 4, -5])
b = np.array([1, 2, 3])

# Diagonals
d1 = a + b
d2 = a - b

# Define parallelogram vertices
O = np.array([0, 0, 0])  # Origin
A = a
B = b
C = a + b  # Opposite vertex

# Setup 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Draw the parallelogram surface
verts = [[O, A, C, B]]
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor="cyan"))

# Plot vectors for sides
ax.quiver(0, 0, 0, a[0], a[1], a[2], color="r", label="a (side)", linewidth=2)
ax.quiver(0, 0, 0, b[0], b[1], b[2], color="g", label="b (side)", linewidth=2)

# Plot diagonals
ax.quiver(0, 0, 0, d1[0], d1[1], d1[2], color="b", linestyle="dashed", label="d1 = a+b")
ax.quiver(0, 0, 0, d2[0], d2[1], d2[2], color="m", linestyle="dashed", label="d2 = a-b")

# Set labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Parallelogram with Sides and Diagonals")

# Auto scale
max_range = np.array([a, b, d1, d2]).max() - np.array([a, b, d1, d2]).min()
Xb = np.array([O[0], A[0], B[0], C[0], d1[0], d2[0]])
Yb = np.array([O[1], A[1], B[1], C[1], d1[1], d2[1]])
Zb = np.array([O[2], A[2], B[2], C[2], d1[2], d2[2]])

ax.set_xlim([Xb.min()-1, Xb.max()+1])
ax.set_ylim([Yb.min()-1, Yb.max()+1])
ax.set_zlim([Zb.min()-1, Zb.max()+1])

ax.legend()

# Save figure
plt.savefig("parallelogram.png", dpi=300)
plt.show()

