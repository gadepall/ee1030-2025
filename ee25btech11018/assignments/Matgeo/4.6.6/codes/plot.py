import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def plane_from_points(A, B, C):
    AB = np.array(B) - np.array(A)
    AC = np.array(C) - np.array(A)
    n = np.cross(AB, AC)
    d = -np.dot(n, A)
    return n, d

def parallel_plane_through_point(n, d, P):
    d_new = -np.dot(n, P)
    return n, d_new

def plane_distance(n, d1, d2):
    return abs(d1 - d2) / np.linalg.norm(n)

# Given points
A = [1, 1, -2]
B = [2, -1, 1]
C = [1, 2, 1]
P = [2, 3, 7]

# Calculate plane coefficients
n1, d1 = plane_from_points(A, B, C)
n2, d2 = parallel_plane_through_point(n1, d1, P)
dist = plane_distance(n1, d1, d2)
print(f"Distance between planes: {dist:.4f}")

# Create mesh grid for plotting planes
xx, yy = np.meshgrid(np.linspace(-3, 4, 30), np.linspace(-3, 5, 30))
zz1 = (-d1 - n1[0]*xx - n1[1]*yy) / n1[2]
zz2 = (-d2 - n2[0]*xx - n2[1]*yy) / n2[2]

# Plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30, azim=60)

# Plot planes with legend
ax.plot_surface(xx, yy, zz1, alpha=0.5, color='blue', label='Plane 1')
ax.plot_surface(xx, yy, zz2, alpha=0.5, color='green', label='Plane 2')

# Plot points directly (no legend entry)
ax.scatter(*zip(*[A, B, C]), color='orange', s=60)
ax.scatter(*P, color='magenta', s=80)

# Mark points clearly with labels
for point, label, color in zip([A, B, C, P], ["A", "B", "C", "P"], ['orange', 'orange', 'orange', 'magenta']):
    ax.text(point[0], point[1], point[2], f'  {label}', color=color, fontsize=12, fontweight='bold')

# Create legend only for planes using proxy artists
legend_elements = [
    Patch(facecolor='blue', edgecolor='r', label='Plane 1'),
    Patch(facecolor='green', edgecolor='r', label='Plane 2'),
]

ax.legend(handles=legend_elements, loc='best')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Two Parallel Planes and Distance = {dist:.4f}")

plt.show()

