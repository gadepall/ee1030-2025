import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==== Define the vectors ====
A = np.array([1, 2, 3])   # example vector A
B = np.array([2, -1, 1])  # example vector B
C = np.array([3, 1, 2])   # example vector C

# Compute normal to the plane (B-A) × (C-A)
normal = np.cross(B - A, C - A)

# Equation of plane: n·(X - A) = 0  →  n·X = n·A
d = np.dot(normal, A)

# ==== Plotting ====
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors A,B,C from origin (with labels for legend)
ax.quiver(0, 0, 0, A[0], A[1], A[2], color='r', label='Vector A')
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='g', label='Vector B')
ax.quiver(0, 0, 0, C[0], C[1], C[2], color='b', label='Vector C')

# Add labels at arrow tips
ax.text(A[0], A[1], A[2], "A", color='r', fontsize=12, weight='bold')
ax.text(B[0], B[1], B[2], "B", color='g', fontsize=12, weight='bold')
ax.text(C[0], C[1], C[2], "C", color='b', fontsize=12, weight='bold')

# Create grid for the plane
xx, yy = np.meshgrid(range(-2, 4), range(-2, 4))
zz = (d - normal[0]*xx - normal[1]*yy) / normal[2]

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Coplanar Vectors and Enclosing Plane")

# Show legend box
ax.legend()

# ==== Save the figure ====
plt.savefig("coplanar_vectors_plane.png", dpi=300, bbox_inches='tight')

plt.show()

